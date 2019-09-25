from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasketPageLocators


class BasketPage(BasePage):
   def should_empty_text(self):
        text_mes = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert 'пуста' in text_mes.text, f"текста не тот {text_mes.text}"