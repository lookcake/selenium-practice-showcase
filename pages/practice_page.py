# src/pages/practice_page.py
from core.base_page import BasePage
from config.settings import BASE_URL
from components.autocomplete import AutoComplete
from components.alerts import Alerts
from components.dropdown import Dropdown
from components.show_hide import ShowHide
from components.web_table import WebTable
from components.hover_menu import HoverMenu
from components.radio_group import RadioGroup
from components.checkbox_group import CheckboxGroup
from components.windows_tabs import WindowsTabs

class PracticePage(BasePage):
    def open(self):
        self.driver.get(BASE_URL)
        return self

    @property
    def radios(self):
        return RadioGroup(self.driver)

    @property
    def checkboxes(self):
        return CheckboxGroup(self.driver)

    @property
    def dropdown(self):
        return Dropdown(self.driver)

    @property
    def autocomplete(self):
        return AutoComplete(self.driver)

    @property
    def alerts(self):
        return Alerts(self.driver)

    @property
    def show_hide(self):
        return ShowHide(self.driver)

    @property
    def web_table(self):
        return WebTable(self.driver)

    @property
    def hover_menu(self):
        return HoverMenu(self.driver)

    @property
    def windows_tabs(self):
        return WindowsTabs(self.driver)
