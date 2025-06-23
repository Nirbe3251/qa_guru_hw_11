import pytest
from selene import browser

@pytest.fixture
def open_browser():
    browser.open("https://demoqa.com/automation-practice-form")
    yield
    browser.quit()