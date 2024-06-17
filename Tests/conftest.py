import configparser
from Utilities.read_config import read_configuration
from Utilities.logger_config import take_screenshots_on_failure, logger
import pytest
from selenium import webdriver

config = configparser.ConfigParser()
config.read('config.ini')


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def driver(request, browser):
    base_url = read_configuration('Default', 'BaseUrl')
    if browser == "chrome":
        driver = webdriver.Chrome()
        window_handle = driver.current_window_handle
        print(f"Current Window Handle: {window_handle}")

    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise Exception("enter valid browser should be chrome or firefox")

    driver.get(base_url)
    driver.refresh()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Pytest hook to take screenshot on test failure.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            screenshot_path = take_screenshots_on_failure(driver, item.name)
            logger.info(f"Screenshot captured on failure: {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {e}")
