class CartPageConstant:
    """Constants related to Cart Page"""

    # Delete from the cart
    DELETE_XPATH = ".//input[@type='checkbox']"
    DELETE_BUTTON_XPATH = ".//input[@name='updatecart']"

    # Messages
    CART_MESSAGE_XPATH = ".//*[contains(text(), 'Product(s)')]"
    CART_MESSAGE_TEXT = 'Product(s)'
    DELETE_MESSAGE_XPATH = ".//*[contains(text(), 'Your Shopping Cart is empty!')]"
    DELETE_MESSAGE_TEXT = "Your Shopping Cart is empty!"
