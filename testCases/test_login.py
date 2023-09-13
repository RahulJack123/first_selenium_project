import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
     # baseURl = "https://opensource-demo.orangehrmlive.com/"
     # username = "Admin"
     # password = "admin123"
    # baseURl = "https://admin-demo.nopcommerce.com/"   # we are directly accessing url here.
     baseURl = ReadConfig.getApplicationURl()        # here we are using config.ini file's data through utilities file
     username = ReadConfig.getUserMail()
     password = ReadConfig.getPassword()

     logger = LogGen.loggen()

     def test_homePageTitle(self):
        self.logger.info("**************Test_001_Login***************")
        self.logger.info("**************verifying Home page title***************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("**************Home page title is passed ***************")
        else:
            assert False


     def test_login(self):
        self.logger.info("*********verifying login test***********")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************Login test passed***************")
        else:
            assert False
