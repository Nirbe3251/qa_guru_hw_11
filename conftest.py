import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from utils import attach



@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = Options()
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            #"enableLog": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    
    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs()
    attach.add_video(browser)

    browser.quit()
