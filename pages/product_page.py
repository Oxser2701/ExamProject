import logging

from selenium.webdriver.common.by import By

from constant.product_page import ProductPageConstant
from helpers.base import BaseHelpers


class ProductPage(BaseHelpers):
    """Store helper methods related to start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constant = ProductPageConstant

    def open_product(self):
        """Open the product"""
        self.driver.find_element_by_xpath(self.constant.PRODUCT_XPATH).click()
        self.log.info("Open the product review")

    def open_review(self):
        """Open review for chosen product"""
        self.driver.find_element_by_xpath(self.constant.REVIEW_XPATH).click()
        self.log.info("Open the product review")

    def add_to_cart(self):
        """Add to the cart chosen product"""
        self.driver.find_element_by_xpath(self.constant.ADD_TO_CART_XPATH).click()
        self.log.info("Add to the cart")

    def fill_title_text(self, title, text):
        """Fill comment form, rate the product and send it"""
        # Enter comment Title
        self.fill_input_field(by=By.XPATH, locator=self.constant.REVIEW_TITLE_XPATH, value=title)
        # Enter comment Text
        self.fill_input_field(by=By.XPATH, locator=self.constant.REVIEW_TEXT_XPATH, value=text)
        self.log.info("Enter Title and Text")
        # Rate the product
        self.open_element(by=By.XPATH, locator=self.constant.REVIEW_RATE_XPATH)
        self.log.info("Rate product")
        # Publish the comment
        self.driver.find_element_by_xpath(self.constant.REVIEW_BUTTON_XPATH).click()

    def verify_message(self, text):
        """Find error message and verify text"""

        message = self.find_by_contains_text(text)
        assert message.text == text
