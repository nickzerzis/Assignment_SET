from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage


class SignUpPage(BasePage):

    NAME_FORM = (By.ID, "fullName")
    EMAIL_FORM_SIGN = (By.ID, "email")
    PWD_FORM_SIGN = (By.ID, "password")
    COMPANY_FORM = (By.ID, "company")
    ADDRESS_FORM = (By.ID, "address")
    SIGN_UP_BTN = (By.NAME, "action")
    SUCCESSFUL_REG = (By.XPATH, "//*[@id='root']/div/div")

    INVALID_MESSAGE_SIGNUP = (By.XPATH, "//*[@id='root']/div/div/div/form/div[2]/div/p")

    def __init__(self):
        super().__init__()

    def enter_name(self, name):
        self.wait_for(self.NAME_FORM)
        self.find_element(self.NAME_FORM).send_keys(name)

    def enter_email_signup(self,email_signup):
        self.find_element(self.EMAIL_FORM_SIGN).send_keys(email_signup)

    def enter_pwd_signup(self,pwd_signup):
        self.find_element(self.PWD_FORM_SIGN).send_keys(pwd_signup)

    def enter_company(self,company):
        self.find_element(self.COMPANY_FORM).send_keys(company)

    def enter_address(self,address):
        self.find_element(self.ADDRESS_FORM).send_keys(address)

    def click_sign_up_btn(self):
        self.find_element(self.SIGN_UP_BTN).click()

    def successful_registration(self):
        self.wait_for(self.SUCCESSFUL_REG)
        return self.find_element(self.SUCCESSFUL_REG).text

    def get_validation_email_msg(self):
        self.wait_for(self.INVALID_MESSAGE_SIGNUP)
        return self.find_element(self.INVALID_MESSAGE_SIGNUP).text


