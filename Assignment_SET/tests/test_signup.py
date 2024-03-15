import pytest
from PageObjects.SignUpPage import SignUpPage
import constants
import time

"""
Sign up tests for user entry in PM Tool

"""
@pytest.mark.signuPositive
def test_user_sign_up_success_with_optional():

        user = SignUpPage()

        # open page
        user.open_page(constants.URL)

        # verify landing
        welcome_message = user.successful_page_landing()
        assert "Welcome to PPM tool" in welcome_message

        user.navigate_to_sign_up_page()
        #fill in
        user.enter_name("Nikos")
        user.enter_email_signup("Nikos@email.com")
        user.enter_pwd_signup("#nick@")
        user.enter_company("CompanyA")
        user.enter_address("Likourgou 100")
        user.click_sign_up_btn()
        time.sleep(5)
        successful_reg = user.successful_registration()

        assert "Successfull registration" in successful_reg, "Registration failed!"

@pytest.mark.signuPositive
def test_user_sign_up_success_without_optional():

        user = SignUpPage()

        # open page
        user.open_page(constants.URL)

        # verify landing
        welcome_message = user.successful_page_landing()
        assert "Welcome to PPM tool" in welcome_message

        user.navigate_to_sign_up_page()
        #fill in
        user.enter_name("John")
        user.enter_email_signup("John@email.gr")
        user.enter_pwd_signup("pass#@")
        user.click_sign_up_btn()
        time.sleep(5)
        successful_reg = user.successful_registration()

        assert "Successfull registration" in successful_reg, "Registration failed!"

@pytest.mark.signupNegative
def test_user_sign_up_blank_email():

        user = SignUpPage()

        # open page
        user.open_page(constants.URL)

        # verify landing
        welcome_message = user.successful_page_landing()
        assert "Welcome to PPM tool" in welcome_message

        user.navigate_to_sign_up_page()
        #fill in
        user.enter_name("Mary")
        user.enter_pwd_signup("password")
        user.enter_company("CompanyB")
        user.enter_address("Likourgou 100")
        user.click_sign_up_btn()
        time.sleep(5)
        validation_email_msg = user.get_validation_email_msg()

        assert "This field is required" in validation_email_msg, "The user probably wrongly allowed to be registered"

@pytest.mark.signupNegative
def test_user_sign_up_wrong_email():

        user = SignUpPage()

        # open page
        user.open_page(constants.URL)

        # verify landing
        welcome_message = user.successful_page_landing()
        assert "Welcome to PPM tool" in welcome_message

        user.navigate_to_sign_up_page()
        #fill in
        user.enter_name("Name2")
        user.enter_email_signup("Name2email.gr")
        user.enter_pwd_signup("pass")
        user.enter_company("Company")
        user.enter_address("Likourgou 100")
        user.click_sign_up_btn()
        time.sleep(5)
        validation_email_msg = user.get_validation_email_msg()

        assert "Invalid email format" in validation_email_msg, "The user probably wrongly allowed to be registered"