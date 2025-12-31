# src/components/dropdown.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from core.base_page import BasePage

class Dropdown(BasePage):
    SELECT = (By.ID, "dropdown-class-example")

    def select_by_value(self, value: str):
        Select(self.find(self.SELECT)).select_by_value(value)

    def selected_text(self) -> str:
        return Select(self.find(self.SELECT)).first_selected_option.text.strip()
