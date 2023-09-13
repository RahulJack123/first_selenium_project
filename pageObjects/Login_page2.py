from selenium import webdriver
from selenium.webdriver.common.by import By



class Login:
    clnic_code_xpath = '//*[@id="clinic"]/span'
    username_xpath = '//*[@id="username"]/span'
    pasword_xpath = '//*[@id="password"]/span'
    login_btn_xpath = '//*[text()="Login"]'
    error_msg = '//*[@class="mtab-login-error-message"]'

    def __init__(self,driver):
        self.driver = webdriver.Chrome()
        self.driver.get()