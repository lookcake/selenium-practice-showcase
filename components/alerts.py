# src/components/alerts.py
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class Alerts(BasePage):
    NAME = (By.ID, "name")
    ALERT_BTN = (By.ID, "alertbtn")
    CONFIRM_BTN = (By.ID, "confirmbtn")

    def input_name(self, name: str):
        self.type(self.NAME, name)

    def trigger_alert_accept(self) -> str:
        self.click(self.ALERT_BTN)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def trigger_confirm_dismiss(self) -> str:
        self.click(self.CONFIRM_BTN)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.dismiss()
        return text
