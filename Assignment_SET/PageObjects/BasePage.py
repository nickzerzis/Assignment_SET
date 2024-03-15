from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage:

    WELCOME_MESSAGE = (By.CLASS_NAME, "card-content")
    LOGIN_PAGE = (By.ID, "login")
    SIGN_UP_PAGE = (By.ID, "signup")

    def __init__(self, driver=r"..\PageObjects" ):
        self.driver = driver
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
           print(f"The element {locator[1]} not found within the given time!")
           self.driver.quit()

    def successful_page_landing(self):
        self.wait_for(self.WELCOME_MESSAGE)
        return self.find_element(self.WELCOME_MESSAGE).text

    def navigate_to_login_page(self):
        self.find_element(self.LOGIN_PAGE).click()

    def navigate_to_sign_up_page(self):
        self.find_element(self.SIGN_UP_PAGE).click()

