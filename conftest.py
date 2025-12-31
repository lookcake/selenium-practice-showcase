# conftest.py
import pytest
from core.driver_factory import create_chrome_driver
from config.settings import DEFAULT_TIMEOUT_SECONDS
from pages.practice_page import PracticePage
from core.artifacts import attach_screenshot, attach_page_source, save_failure_files

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run Chrome in headless mode")

@pytest.fixture
def driver(request):
    headless = request.config.getoption("--headless")
    d = create_chrome_driver(headless=headless)
    yield d
    d.quit()

@pytest.fixture
def practice_page(driver):
    return PracticePage(driver, timeout=DEFAULT_TIMEOUT_SECONDS)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        d = item.funcargs.get("driver")
        if d:
            test_name = item.nodeid.replace("/", "_").replace("::", "__")
            # local artifacts
            save_failure_files(d, test_name=test_name)
            # allure artifacts
            attach_screenshot(d, name="Failure Screenshot")
            attach_page_source(d, name="Failure Page Source")
