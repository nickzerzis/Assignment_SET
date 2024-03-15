from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):

    EMAIL_FORM_LOGIN = (By.ID, "email")
    PWD_FORM_LOGIN = (By.ID, "password")
    LOGIN_BTN = (By.NAME, "action")
    PM_BOX = (By.CSS_SELECTOR,".card-title")
    INVALID_MESSAGE_LOGIN = (By.XPATH, "//*[@id='root']/div/div/div/form/div[2]/div/p")

    def __init__(self):
        super().__init__()

    def enter_email_login(self,email_login):
        self.wait_for(self.EMAIL_FORM_LOGIN)
        self.find_element(self.EMAIL_FORM_LOGIN).send_keys(email_login)

    def enter_pwd_login(self,pwd_login):
        self.find_element(self.PWD_FORM_LOGIN).send_keys(pwd_login)

    def click_login_btn(self):
        self.find_element(self.LOGIN_BTN).click()

    def successful_login(self):
        self.wait_for(self.PM_BOX)
        return self.find_element(self.PM_BOX).is_displayed()

    def get_validation_login_msg(self):
        self.wait_for(self.INVALID_MESSAGE_LOGIN)
        return self.find_element(self.INVALID_MESSAGE_LOGIN).text

    def user_login(self,email,password,url):
        self.open_page(url)
        self.navigate_to_login_page()
        self.wait_for(self.EMAIL_FORM_LOGIN)
        self.find_element(self.EMAIL_FORM_LOGIN).send_keys(email)
        self.find_element(self.PWD_FORM_LOGIN).send_keys(password)
        self.find_element(self.LOGIN_BTN).click()


