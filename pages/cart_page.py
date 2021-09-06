import logging

from constant.cart_page import CartPageConstant
from helpers.base import BaseHelpers


class CartPage(BaseHelpers):
    """Store helper methods related to start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constant = CartPageConstant

    def delete_product(self):
        """Deleting an item from the cart"""
        # Select item to delete
        self.driver.find_element_by_xpath(self.constant.DELETE_XPATH).click()
        # Click on the delete button
        self.driver.find_element_by_xpath(self.constant.DELETE_BUTTON_XPATH).click()

    def verify_message(self, text):
        """Find error message and verify text"""

        message = self.find_by_contains_text(text)
        assert message.text == text
