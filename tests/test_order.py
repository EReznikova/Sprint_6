from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import OrderPage
from pages.main_page import MainPage

import pytest
import allure

class TestOrder:
    @pytest.mark.parametrize(
    "order_button, name, last_name, address, metro, phone",
    [
        (
            "top",
            "Анна",
            "Иванова",
            "Москва, Тверская 1",
            "Сокольники",
            "+79151234567",
        ),
        (
            "bottom",
            "Мария",
            "Петрова",
            "Москва, Арбат 10",
            "Охотный Ряд",
            "+79261234567",
        ),
    ],
        ids=["верхняя_кнопка", "нижняя_кнопка"],
    )
    def test_order(
        self,
        driver,
        order_button,
        name,
        last_name,
        address,
        metro,
        phone,
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()

        if order_button == "top":
            main_page.order_top_click()
        else:
            main_page.order_bottom_click()

        order_page.fill_name(name)
        order_page.fill_last_name(last_name)
        order_page.fill_address(address)
        order_page.select_metro(metro)
        order_page.fill_phone(phone)
        order_page.next_button_click()

        order_page.fill_date("01.01.2027")
        order_page.select_rental_period("сутки")
        order_page.select_black_color()
        order_page.fill_comment("Позвонить за час")
        order_page.click_order_button()
        order_page.confirm_order()

        assert order_page.is_order_created()

    def test_scooter_logo(self, driver):  
        main_page = MainPage(driver)
        main_page.open()
        main_page.scooter_logo_click();
        assert driver.current_url == main_page.URL

    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        original_window = driver.current_window_handle

        main_page.yandex_logo_click()

        WebDriverWait(driver, 10).until(
            EC.number_of_windows_to_be(2)
        )

        new_window = next(
            window for window in driver.window_handles
            if window != original_window
        )
        driver.switch_to.window(new_window)

        WebDriverWait(driver, 10).until(
            EC.url_contains("ya.ru")
        )

        assert "ya.ru" in driver.current_url
                  

