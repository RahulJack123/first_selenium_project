from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



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
    txt_DoB_xpath  = "// input[@ id='DateOfBirth']"
    txt_company_xpath = "// input[@ id='Company']"
    ckbx_isTaxExempt_xpath = "// input[@ id='IsTaxExempt']"
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



