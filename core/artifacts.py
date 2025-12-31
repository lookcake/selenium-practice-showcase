# src/core/artifacts.py
from pathlib import Path
import allure
from config.settings import ARTIFACTS_DIR

def ensure_artifacts_dir() -> Path:
    p = Path(ARTIFACTS_DIR)
    p.mkdir(parents=True, exist_ok=True)
    return p

def attach_screenshot(driver, name: str = "screenshot"):
    png = driver.get_screenshot_as_png()
    allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)

def attach_page_source(driver, name: str = "page_source"):
    html = driver.page_source
    allure.attach(html, name=name, attachment_type=allure.attachment_type.HTML)

def save_failure_files(driver, test_name: str):
    p = ensure_artifacts_dir()
    screenshot_path = p / f"{test_name}.png"
    html_path = p / f"{test_name}.html"
    driver.save_screenshot(str(screenshot_path))
    html_path.write_text(driver.page_source, encoding="utf-8")
