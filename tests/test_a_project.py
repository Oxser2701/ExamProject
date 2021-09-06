import pytest

from conftest import BaseTest
from constant.login_page import LoginPageConstant
from helpers.base import UserData

"""Registration and login tests"""


class TestProject(BaseTest):

    @pytest.fixture(scope='function')
    def registered_user(self, start_page, user):
        profile = start_page.register_user(user)
        profile.logout()
        return user

    def test_empty_values(self, start_page):
        """
        - Open start page
        - Fill empty values and click Login button
        - Verify error message
        """
        start_page.login(UserData())
        start_page.verify_message(LoginPageConstant.ERROR_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_incorrect_values(self, start_page, user: UserData):
        """
        - Open start page
        - Open Login form and enter incorrect values
        - Verify error message
        """
        start_page.login(user)
        start_page.verify_message(LoginPageConstant.ERROR_LOGIN_MESSAGE_TEXT)
        self.log.info("Error message")

    def test_register_account(self, start_page, logout, user):
        """
        - Open start page
        - Open Register form and fill all necessary fields
        - Verify successful registration
        """
        profile = start_page.register_user(user)
        profile.verify_message(text=user.email)
        self.log.info("Registration was success and verified")

    def test_login(self, registered_user, start_page, logout):
        """
        - Open start page
        - Open Login form and enter correct values
        - Verify success login
        """
        profile = start_page.login(registered_user)
        profile.verify_message(registered_user.email)
        self.log.info("Registration was success and verified")
