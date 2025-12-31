# src/core/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_chrome_driver(headless: bool = False) -> webdriver.Chrome:
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    if headless:
        # New headless mode
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    return driver
