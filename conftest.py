import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.page_load_strategy = "eager"
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture(scope="class")
def faq_page():
    browser = webdriver.Firefox()
    browser.maximize_window()

    page = MainPage(browser)
    page.open()
    page.confirm_click()

    yield page

    browser.quit()
