import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope = "function", autouse=True)
def open_browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    browser.config.window_height = 1024
    browser.config.window_width = 1024
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = options
    yield
    browser.quit()