from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By


class AddCustomer:
    lnk_customer_menu_xpath = "// *[ @ href = '#'] and [ @class ='nav-link']"
    lnk_customer_sbmenu_xpath = "// li[@ class ='nav-item has-treeview menu-is-opening menu-open'] // li[1] // a[1]"
    btnAddnew_xpath = "// a[@ class ='btn btn-primary']"
    txt_Email_xpath = "// input[@ id='Email']"
    txt_Password_xpath = "// input[@ id='Password']"
    txt_FirstName_xpath = "// input[@ id='FirstName']"
    txt_LastName_xpath = "// input[@ id='LastName']"
    rbtn_Gender_Male_xpath = "// input[@ id='Gender_Male']"
    rbtn_Gender_Female_xpath = "// input[@ id='Gender_Female']"
    txt_DoB_xpath = "// input[@ id='DateOfBirth']"
    txt_company_xpath = "// input[@ id='Company']"
    ckbx_taxexempt_xpath = "// input[@ id='IsTaxExempt']"
    list_newsletter_xpath = '// *[@ id="customer-info"] / div[2] / div[9] / div[2]'
    txt_CustomerRole_xpath = '// *[@ id="customer-info"] / div[2] / div[10] / div[2]'
    list_custRoleItem_adminstr_xpath = '// *[@ id="SelectedCustomerRoleIds"] / option[1]'
    list_custRoleItem_formmodultr_xpath = '// *[@ id="SelectedCustomerRoleIds"] / option[2]'
    list_custRoleItem_guiest_xpath = '// *[@ id="SelectedCustomerRoleIds"] / option[3]'
    list_custRoleItem_registered_xpath = '// *[@ id="SelectedCustomerRoleIds"] / option[4]'
    list_custRoleItem_vender_xpath = '// *[@ id="SelectedCustomerRoleIds"] / option[5]'
    drp_mangrofVendor_xpath = "// select[@ id='VendorId']"
    drp_mangrVndrItem1_xpath = "// option[normalize-space()='Vendor 1']"
    drp_mangrVndrItem2_xpath = "// option[normalize-space()='Vendor 2']"
    ckbx_active_xpath = '// *[@ id="customer-info"] / div[2] / div[12] / div[2]'
    txt_AdminComment_xpath = "// textarea[@ id='AdminComment']"
    btn_save_xpath = "// button[@ name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_sbmenu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_Email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_Password_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txt_FirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txt_LastName_xpath).send_keys(lastname)

    def setGenderMale(self):
        self.driver.find_element(By.XPATH,self.rbtn_Gender_Male_xpath).click()

    def setGenderFemale(self):
        self.driver.find_element(By.XPATH,self.rbtn_Gender_Female_xpath).click()

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txt_DoB_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element(By.XPATH,self.txt_company_xpath).send_keys(companyname)

    def setTaxExempt(self):
        self.driver.find_element(By.XPATH,self.ckbx_taxexempt_xpath).click()

    def setNewsLetter(self):
        self.driver.find_element(By.XPATH,self.list_newsletter_xpath).click()

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH,self.txt_CustomerRole_xpath).click()
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.list_custRoleItem_registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.list_custRoleItem_adminstr_xpath)
        elif role == 'Form Moderator':
            self.listitem = self.driver.find_element(By.XPATH,self.list_custRoleItem_formmodultr_xpath)
        elif role == 'Guest':
            self.listitem = self.driver.find_element(By.XPATH,self.list_custRoleItem_guiest_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.list_custRoleItem_vender_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.list_custRoleItem_guiest_xpath)
        self.listitem.click()

    def setManagerofVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drp_mangrofVendor_xpath))
        drp.select_by_visible_text(value)


    def setisActive(self):
        self.driver.find_element(By.XPATH,self.ckbx_active_xpath).click()

    def setAdminComment(self,comment):
        self.driver.find_element(By.XPATH,self.txt_AdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()
