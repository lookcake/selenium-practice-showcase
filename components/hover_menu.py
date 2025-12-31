# src/components/hover_menu.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from core.base_page import BasePage

class HoverMenu(BasePage):
    HOVER_BTN = (By.ID, "mousehover")
    MENU = (By.CSS_SELECTOR, ".mouse-hover-content")
    TOP_LINK = (By.LINK_TEXT, "Top")
    RELOAD_LINK = (By.LINK_TEXT, "Reload")

    def open_menu(self):
        btn = self.find(self.HOVER_BTN)
        ActionChains(self.driver).move_to_element(btn).perform()
        self.waits.visible(self.MENU)

    def click_top(self):
        self.open_menu()
        self.click(self.TOP_LINK)

    def click_reload(self):
        self.open_menu()
        self.click(self.RELOAD_LINK)
