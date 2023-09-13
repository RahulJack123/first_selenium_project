from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_xpath = '//input[@id="Email" and @name="Email"]'
    textbox_password_xpath = '//input[@value="admin" and @name="Password"]'
    button_login_xpath = '//button[@type="submit"]'
    link_logout_linktext = '//*[@id="navbarText"]/ul/li[3]/a'


    def __init__(self,driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()


    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()
