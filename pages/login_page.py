import logging

from selenium.webdriver.common.by import By

from constant.base import BaseConstant
from constant.login_page import LoginPageConstant
from constant.start_page import StartPageConstant
from helpers.base import BaseHelpers, UserData
from pages.start_page import StartPage


class LoginPage(BaseHelpers):
    """Store helper methods related to login page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constant = LoginPageConstant

    def login(self, user: UserData):
        """Login using provided credentials"""
        # Clear required fields and fill
        self.driver.get(BaseConstant.START_PAGE)
        self.log.debug("Open page")
        self.open_element(By.XPATH, StartPageConstant.LOGIN_BUTTON_XPATH)
        self.fill_input_field(by=By.XPATH, locator=self.constant.LOGIN_EMAIL_XPATH, value=user.email)
        self.fill_input_field(by=By.XPATH, locator=self.constant.LOGIN_PASSWORD_XPATH, value=user.password)
        self.log.debug("Fields are filled with invalid values")

        # Click on Sign In button
        self.wait_and_click(By.XPATH, self.constant.LOGIN_BUTTON_XPATH)
        self.log.info("Clicked on 'Sign In'")

        return StartPage(self.driver)

    def register_user(self, user: UserData):
        """Fill required fields and press button"""

        # Open start page
        self.driver.get(BaseConstant.START_PAGE)
        self.log.debug("Open page")
        self.open_element(by=By.XPATH, locator=StartPageConstant.REGISTER_BUTTON_XPATH)

        # Fill fields
        self.fill_input_field(by=By.XPATH, locator=self.constant.REGISTER_FIRSTNAME_XPATH, value=user.firstname)
        self.fill_input_field(by=By.XPATH, locator=self.constant.REGISTER_LASTNAME_XPATH, value=user.lastname)
        self.fill_input_field(by=By.XPATH, locator=self.constant.REGISTER_EMAIL_XPATH, value=user.email)
        self.fill_input_field(by=By.XPATH, locator=self.constant.REGISTER_PASSWORD_XPATH, value=user.password)
        self.fill_input_field(by=By.XPATH, locator=self.constant.REGISTER_CONFIRM_PASSWORD_XPATH, value=user.confirm_password)
        self.log.debug("Fields were filled")

        # Click on Sign Up button
        self.wait_and_click(By.XPATH, LoginPageConstant.REGISTER_BUTTON_XPATH)
        self.wait_and_click(By.XPATH, LoginPageConstant.CONTINUE_BUTTON_XPATH)

        return StartPage(self.driver)

    def verify_message(self, text):
        """Find error message and verify text"""

        message = self.find_by_contains_text(text)
        assert message.text == text
