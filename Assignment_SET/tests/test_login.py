from PageObjects.LoginPage import LoginPage
import time
import pytest
import constants


"""

Login tests for user entry in PM Tool

"""

@pytest.mark.loginPositive
@pytest.mark.parametrize("email,password", [("nick@email.gr", "password"),("John@email.gr", "pass#@"),("mary@email.com", "maryone")])
def test_user_login_success(email,password):

        """
        Three registered users try to log in
        """

        user = LoginPage()

        # open page
        user.open_page(constants.URL)

        # verify landing
        welcome_message = user.successful_page_landing()
        assert "Welcome to PPM tool" in welcome_message

        user.navigate_to_login_page()
        #fill in
        user.enter_email_login(email)
        user.enter_pwd_login(password)
        user.click_login_btn()
        time.sleep(5)

        assert user.successful_login(), "User is not registered!"

@pytest.mark.loginNegative
@pytest.mark.parametrize("email,password", [("user1@email.gr", "password"),("user2@email.gr", "pass"),("mary@email.com", "marytwo")])
def test_user_login_fail(email,password):

        """
        Three non-registered users try to log in
        """

        user = LoginPage()

        # open page
        user.open_page(constants.URL)

        # verify landing
        welcome_message = user.successful_page_landing()
        assert "Welcome to PPM tool" in welcome_message

        user.navigate_to_login_page()
        #fill in
        user.enter_email_login(email)
        user.enter_pwd_login(password)
        user.click_login_btn()
        time.sleep(5)

        validation_login_msg = user.get_validation_login_msg()

        assert "Invalid login info" in validation_login_msg