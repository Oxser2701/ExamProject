class LoginPageConstant:
    """Constants related to Login Page"""

    # Login
    LOGIN_EMAIL_XPATH = ".//input[@id='Email']"
    LOGIN_PASSWORD_XPATH = ".//input[@id='Password']"
    LOGIN_BUTTON_XPATH = ".//input[@value='Log in']"

    # Register
    REGISTER_FIRSTNAME_XPATH = ".//input[@id='FirstName']"
    REGISTER_LASTNAME_XPATH = ".//input[@id='LastName']"
    REGISTER_EMAIL_XPATH = ".//input[@id='Email']"
    REGISTER_PASSWORD_XPATH = ".//input[@id='Password']"
    REGISTER_CONFIRM_PASSWORD_XPATH = ".//input[@id='ConfirmPassword']"
    REGISTER_BUTTON_XPATH = ".//input[@id='register-button']"
    CONTINUE_BUTTON_XPATH = ".//div[@class='buttons']//input[@value='Continue']"

    # Messages
    ERROR_LOGIN_MESSAGE_XPATH = ".//*[contains(text(), 'No customer account found')]"
    ERROR_LOGIN_MESSAGE_TEXT = 'No customer account found'
    COMPLETE_REGISTRATION_XPATH = ".//*[contains(text(), 'Your registration completed')]"
    COMPLETE_REGISTRATION_TEXT = 'Your registration completed'
    COMPLETE_LOGIN_XPATH = ".//a[@class='account']"
    COMPLETE_LOGIN_TEXT = 'test@project.com'
