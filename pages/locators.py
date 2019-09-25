from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    IN_BUT = (By.CSS_SELECTOR, '[name="login_submit"]')
    EMAIL_AREA = (By.CSS_SELECTOR, '[name="login-username"]')
    PASS_AREA = (By.CSS_SELECTOR, '[name="login-password"]')
    LOGIN_FORM = (By.ID, 'login_form')
    REG_FORM = (By.ID, 'register_form')
    REG_EMAIL_AREA = (By.NAME, 'registration-email')
    REG_PAS_AREA = (By.NAME, 'registration-password1')
    REG_PAS_REPEAT_AREA = (By.NAME, 'registration-password2')
    REG_BUT = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUM_IN_BASKET = (By.CSS_SELECTOR, '.alertinner >p>strong')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PROD_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PROD_ADD = (By.CSS_SELECTOR, '.alert-success:nth-child(1)>.alertinner>strong')
    MES_SUCCESS = (By.CSS_SELECTOR, 'sdas')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_BASKET = (By.CSS_SELECTOR, '.btn-group>a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCT = (By.CSS_SELECTOR, '.basket-items')
    BASKET_HEAD = (By.CSS_SELECTOR, '.page-header>h1')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')
