class StartPageConstant:
    """Constants related to Start Page"""

    # Login/Logout/Register/Cart buttons
    LOGIN_BUTTON_XPATH = ".//a[@href='/login']"
    LOGOUT_BUTTON_XPATH = ".//a[@href='/logout']"
    REGISTER_BUTTON_XPATH = ".//a[@href='/register']"
    OPEN_CART_XPATH = ".//a[@href='/cart']"

    # Review message
    REVIEW_MESSAGE_XPATH = ".//div[@class='result' and contains(text(), 'Product review is successfully added.')]"
    REVIEW_MESSAGE_TEXT = "Product review is successfully added."
