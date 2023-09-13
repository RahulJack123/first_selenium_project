import pytest
import time
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_002_AddCustomer:
    baseURl = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_addCustomer(self, setup,):
        self.driver = setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        time.sleep(60)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()

        self.addcust.setEmail("rahul@gmail.com")
        self.addcust.setPassword("rahul123")
        self.addcust.setFirstName("rahul")
        self.addcust.setLastName("bharti")
        self.addcust.setGenderMale()
        self.addcust.setDob("10/08/1990")
        self.addcust.setCompanyName("TechMahindra")
        self.addcust.setTaxExempt()
        self.addcust.setNewsLetter()
        self.addcust.setCustomerRole("Guest")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setisActive()
        self.addcust.setAdminComment("this is test for my automation project")
        self.addcust.clickOnSave()

        print(self.driver.title)


time.sleep(10)