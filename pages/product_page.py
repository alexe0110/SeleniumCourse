from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage(BasePage):
    def add_basket(self):
        but_add = self.browser.find_element(*ProductPageLocators.ADD)
        but_add.click()

    def should_in_basket(self):
        summ = self.browser.find_element(*ProductPageLocators.SUM_IN_BASKET)
        price = self.browser.find_element(*ProductPageLocators.PRICE)

        assert summ.text == price.text, f"цена и корзина не совпадают {print(summ)} and {print(price)}"

    def should_message_add(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PROD_NAME)
        prod_add = self.browser.find_element(*ProductPageLocators.PROD_ADD)

        assert prod_name.text == prod_add.text, f"Товары не совпадают {prod_name.text} and {prod_add.text}"
