from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    IN_BUT = (By.CSS_SELECTOR, '[name="login_submit"]')
    EMAIL_AREA = (By.CSS_SELECTOR, '[name="login-username"]')
    PASS_AREA = (By.CSS_SELECTOR, '[name="login-password"]')
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')