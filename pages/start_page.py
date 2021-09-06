import logging

from selenium.webdriver.common.by import By

from constant.start_page import StartPageConstant
from helpers.base import BaseHelpers


class StartPage(BaseHelpers):
    """Store helper methods related to start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constant = StartPageConstant

    def open_cart(self):
        """Open cart"""
        self.driver.find_element_by_xpath(self.constant.OPEN_CART_XPATH).click()
        self.log.info("Cart is opened")

    def logout(self):
        """Logout from the user's account"""
        self.wait_and_click(By.XPATH, self.constant.LOGOUT_BUTTON_XPATH)
        self.log.info("Logged out")

    def verify_message(self, text):
        """Find error message and verify text"""

        message = self.find_by_contains_text(text)
        assert message.text == text
