# src/components/windows_tabs.py
from selenium.webdriver.common.by import By
from core.base_page import BasePage
from core.window_manager import WindowManager

class WindowsTabs(BasePage):
    OPEN_WINDOW = (By.ID, "openwindow")
    OPEN_TAB = (By.ID, "opentab")

    def open_window_and_close(self):
        wm = WindowManager(self.driver)
        original = wm.current_handle()

        self.click(self.OPEN_WINDOW)
        wm.switch_to_newest()

        # just assert we switched by checking title exists
        _ = self.driver.title

        wm.close_current_and_back(original)

    def open_tab_and_close(self):
        wm = WindowManager(self.driver)
        original = wm.current_handle()

        self.click(self.OPEN_TAB)
        wm.switch_to_newest()
        _ = self.driver.title

        wm.close_current_and_back(original)
