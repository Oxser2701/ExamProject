class ProductPageConstant:
    """Constants related to Product Page"""

    # Review product

    REVIEW_TITLE_XPATH = ".//input[@class='review-title']"
    REVIEW_TEXT_XPATH = ".//textarea[@class='review-text']"
    REVIEW_RATE_XPATH = ".//input[@checked='checked' and @type='radio' and @value='5']"
    REVIEW_BUTTON_XPATH = ".//input[@name='add-review']"
    PRODUCT_XPATH = ".//a[@href='/141-inch-laptop']"
    REVIEW_XPATH = ".//a[@href='/productreviews/31']"

    # Review message
    REVIEW_MESSAGE_XPATH = ".//div[@class='result' and contains(text(), 'Product review is successfully added.')]"
    REVIEW_MESSAGE_TEXT = "Product review is successfully added."

    # Buy Product

    ADD_TO_CART_XPATH = ".//input[@id='add-to-cart-button-31']"
