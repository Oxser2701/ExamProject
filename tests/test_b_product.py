import pytest

from conftest import BaseTest
from constant.cart_page import CartPageConstant
from constant.product_page import ProductPageConstant
from helpers.base import generate_text
from pages.cart_page import CartPage
from pages.product_page import ProductPage

"""Reviewing, buying and deleting products tests"""


class TestComment(BaseTest):

    @pytest.fixture(scope='function')
    def registered_user(self, start_page, user):
        profile = start_page.register_user(user)
        profile.logout()
        return user

    def test_text_comment(self, start_page, registered_user, logout):
        """
        - Open the page
        - Open an item
        - Open review form
        - Text some comment
        - Rate the item
        - Submit review
        """
        profile = start_page.login(registered_user)
        create_comment = ProductPage(profile.driver)
        create_comment.open_product()
        create_comment.open_review()
        title = "Test Title. Welcome to my review"
        text = generate_text(100)
        create_comment.fill_title_text(title=title, text=text)
        create_comment.verify_message(ProductPageConstant.REVIEW_MESSAGE_TEXT)
        self.log.info("Comment was successfully added")

    def test_adding_to_cart(self, start_page, registered_user, logout):
        """
        - Open the page
        - Select a product
        - Add to cart
        - Verify, that chosen product in the cart
        """
        profile = start_page.login(registered_user)
        buy = ProductPage(profile.driver)
        buy.open_product()
        buy.add_to_cart()
        profile.open_cart()
        buy.verify_message(CartPageConstant.CART_MESSAGE_TEXT)
        self.log.info("Product was successfully added to the cart")

    def test_deleting_from_cart(self, start_page, registered_user):
        """
        - Open the page
        - Open cart
        - Delete the item
        - Verify, that item was deleted
        - Logout
        """
        profile = start_page.login(registered_user)
        buy = ProductPage(profile.driver)
        buy.open_product()
        buy.add_to_cart()
        profile.open_cart()
        remove = CartPage(profile.driver)
        remove.delete_product()
        remove.verify_message(CartPageConstant.DELETE_MESSAGE_TEXT)
        profile.logout()
        self.log.info("Product was successfully deleted from the cart")
