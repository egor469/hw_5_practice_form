import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 1024
    browser.open('https://demoqa.com/automation-practice-form')

    yield
    browser.quit()