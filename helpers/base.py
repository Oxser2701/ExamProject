import random

import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constant.text_base import TEXTS


def generate_text(word_count=5, lang="eng"):
    """Generate random text based sample text"""
    text = TEXTS[lang].replace("\n", "").split(" ")
    generated_text_lst = []
    for _ in range(word_count):
        generated_text_lst.append(random.choice(text))
    generated_text = ' '.join(generated_text_lst)
    return generated_text


class BaseHelpers:
    """Store base helpers for Web testing"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    def wait_until_element_find(self, locator_type, locator):
        """Wait until element find and return it"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    def wait_and_click(self, locator_type, locator):
        """Wait until element clickable and click"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        self.driver.find_element(by=locator_type, value=locator).click()

    def fill_input_field(self, by, locator, value=""):
        """Find required element using by.X model, clear input field and enter the value"""

        field = self.wait_until_element_find(locator_type=by, locator=locator)
        field.clear()
        field.send_keys(value)

    def find_by_contains_text(self, text, element_tag="*"):
        """Find element using XPATH contains function by text"""
        return self.wait_until_element_find(By.XPATH, f".//{element_tag}[contains(text(), '{text}')]")

    def open_element(self, by, locator):
        self.wait_and_click(locator_type=by, locator=locator)


class UserData:
    """Store user data useful for Sign In and Sign Up forms"""

    def __init__(self, firstname="", lastname="", email="", password="", confirm_password=""):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
