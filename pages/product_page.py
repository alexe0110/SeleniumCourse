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
        time.sleep(7)
        # summ = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(*ProductPageLocators.SUM_IN_BASKET))
        # price = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(*ProductPageLocators.PRICE))
        summ = self.browser.find_element(*ProductPageLocators.SUM_IN_BASKET)
        price = self.browser.find_element(*ProductPageLocators.PRICE)

        assert summ.text == price.text, f"цена и корзина не совпадают {print(summ)} and {print(price)}"
