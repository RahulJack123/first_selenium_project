from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Admin_add_user import Admin_add_user
from pageObjects.LoginPage import Login
import pytest


class Test_001_Adduser:
    baseURl = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"

    def test_first(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(20)
        self.addcust = Admin_add_user(self.driver)
        self.addcust.clickOnAdmin()
        self.addcust.clickOnAddbtn()
        self.addcust.setUserRole("Admin")
        self.addcust.setEmpName("Rahul")
        self.addcust.setStatus("Enabled")
        self.addcust.setUserName("Rahul123")
        self.addcust.setPasword("Rahul@123")
        self.addcust.setCnfPswd("Rahul@123")
        self.addcust.clickOnSave()

