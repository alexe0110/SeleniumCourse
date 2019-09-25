from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "login is not find"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM)

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REG_EMAIL_AREA)
        pas1 = self.browser.find_element(*LoginPageLocators.REG_PAS_AREA)
        pas2 = self.browser.find_element(*LoginPageLocators.REG_PAS_REPEAT_AREA)
        but = self.browser.find_element(*LoginPageLocators.REG_BUT)

        mail.send_keys(email)
        pas1.send_keys(password)
        pas2.send_keys(password)
        but.click()
