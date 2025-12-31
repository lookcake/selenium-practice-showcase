# src/components/autocomplete.py
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class AutoComplete(BasePage):
    INPUT = (By.ID, "autocomplete")
    MENU = (By.ID, "ui-id-1")

    def type_keyword(self, text: str):
        self.type(self.INPUT, text)

    def pick(self, full_text: str):
        self.waits.visible(self.MENU)
        option = (
            By.XPATH,
            f"//ul[@id='ui-id-1']//li[normalize-space(.)='{full_text}' or .//*[normalize-space(.)='{full_text}']]"
        )
        self.click(option)

    def current_value(self) -> str:
        el = self.find(self.INPUT)
        return el.get_attribute("value") or ""
