# src/components/web_table.py
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class WebTable(BasePage):
    FIXED_TABLE_ROWS = (By.XPATH, "//div[contains(@class,'tableFixHead')]//tbody/tr")
    TOTAL_TEXT = (By.CSS_SELECTOR, ".totalAmount")

    def fixed_table_amounts(self) -> list[int]:
        rows = self.driver.find_elements(*self.FIXED_TABLE_ROWS)
        amounts: list[int] = []
        for r in rows:
            tds = r.find_elements(By.TAG_NAME, "td")
            amounts.append(int(tds[-1].text.strip()))
        return amounts

    def displayed_total(self) -> int:
        text = self.text_of(self.TOTAL_TEXT)  # "Total Amount Collected: 296"
        return int(text.split(":")[-1].strip())
