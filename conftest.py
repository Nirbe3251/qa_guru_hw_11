import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

@pytest.fixture
def open_browser():
    browser.open("https://demoqa.com/automation-practice-form")
    yield
    browser.quit()