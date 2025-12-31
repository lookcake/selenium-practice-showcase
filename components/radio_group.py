# src/components/radio_group.py
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class RadioGroup(BasePage):
    RADIOS = (By.CSS_SELECTOR, "input.radioButton")

    def select_by_value(self, value: str):
        locator = (By.CSS_SELECTOR, f"input.radioButton[value='{value}']")
        self.click(locator)

    def selected_value(self) -> str | None:
        radios = self.driver.find_elements(*self.RADIOS)
        for r in radios:
            if r.is_selected():
                return r.get_attribute("value")
        return None
