from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Admin_add_user:
    tab_admin_xpath = "//aside[@class='oxd-sidepanel']//li[1]"
    button_add_xpath = "//button[normalize-space()='Add']"
    dpdn_userrole_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]"
    textbox_empName_xpath = "//input[@placeholder='Type for hints...']"
    dpdn_status_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]"
    textbox_username_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    textbox_pswd_xpath = "(//input[@type='password'])[1]"
    textbox_cnfpswd_xpath = '(//input[@type="password"])[2]'
    button_save_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnAdmin(self):
        self.driver.find_element(By.XPATH,self.tab_admin_xpath).click()

    def clickOnAddbtn(self):
        self.driver.find_element(By.XPATH,self.button_add_xpath).click()

    def setUserRole(self, userrole):
        drp = Select(self.driver.find_element(By.XPATH,self.dpdn_userrole_xpath))
        drp.select_by_value(userrole)

    def setEmpName(self,name):
        self.driver.find_element(By.XPATH,self.textbox_empName_xpath).send_keys(name)

    def setStatus(self,status):
        drp2 = Select(self.driver.find_element(By.XPATH,self.dpdn_status_xpath))
        drp2.select_by_value(status)

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPasword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_pswd_xpath).send_keys(password)

    def setCnfPswd(self,password2):
        self.driver.find_element(By.XPATH,self.textbox_cnfpswd_xpath).send_keys(password2)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()


