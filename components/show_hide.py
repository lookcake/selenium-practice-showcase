# src/components/show_hide.py
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class ShowHide(BasePage):
    HIDE = (By.ID, "hide-textbox")
    SHOW = (By.ID, "show-textbox")
    TEXTBOX = (By.ID, "displayed-text")

    def hide(self):
        self.click(self.HIDE)
        self.waits.invisible(self.TEXTBOX)

    def show(self):
        self.click(self.SHOW)
        self.waits.visible(self.TEXTBOX)

    def is_visible(self) -> bool:
        try:
            return self.driver.find_element(*self.TEXTBOX).is_displayed()
        except Exception:
            return False
