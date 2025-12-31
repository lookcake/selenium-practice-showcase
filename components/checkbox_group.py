# src/components/checkbox_group.py
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class CheckboxGroup(BasePage):
    CB1 = (By.ID, "checkBoxOption1")
    CB2 = (By.ID, "checkBoxOption2")
    CB3 = (By.ID, "checkBoxOption3")

    def set_option(self, option: int, checked: bool):
        locator = {1: self.CB1, 2: self.CB2, 3: self.CB3}[option]
        el = self.find(locator)
        if el.is_selected() != checked:
            self.click(locator)

    def selected_options(self) -> list[str]:
        options = []
        for loc in [self.CB1, self.CB2, self.CB3]:
            el = self.find(loc)
            if el.is_selected():
                options.append(el.get_attribute("value"))
        return options
