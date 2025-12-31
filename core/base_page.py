# src/core/base_page.py
from selenium.common.exceptions import StaleElementReferenceException
from core.waits import Waits

class BasePage:
    """
    Design principles:
    - Never cache WebElement. Store locators only.
    - Each action re-locates elements to reduce stale element issues.
    """
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.waits = Waits(driver, timeout)

    def find(self, locator):
        return self.waits.presence(locator)

    def click(self, locator):
        for _ in range(2):  # small retry for SPA-ish re-render
            try:
                el = self.waits.clickable(locator)
                el.click()
                return
            except StaleElementReferenceException:
                continue
        # last try - raise if still failing
        el = self.waits.clickable(locator)
        el.click()

    def type(self, locator, text: str, clear: bool = True):
        for _ in range(2):
            try:
                el = self.waits.visible(locator)
                if clear:
                    el.clear()
                el.send_keys(text)
                return
            except StaleElementReferenceException:
                continue
        el = self.waits.visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    def text_of(self, locator) -> str:
        el = self.waits.visible(locator)
        return el.text.strip()
