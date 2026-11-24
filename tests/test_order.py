import allure
from data.order_data import BOTTOM_ORDER_DATA, TOP_ORDER_DATA

class TestOrder:
    @allure.title("Проверка верхней кнопки")
    def test_order_top_button(self, main_page, order_page):
        main_page.open()
        main_page.order_top_click()

        order_page.fill_name(TOP_ORDER_DATA["name"])
        order_page.fill_last_name(TOP_ORDER_DATA["last_name"])
        order_page.fill_address(TOP_ORDER_DATA["address"])
        order_page.select_metro(TOP_ORDER_DATA["metro"])
        order_page.fill_phone(TOP_ORDER_DATA["phone"])
        order_page.next_button_click()

        order_page.fill_date(TOP_ORDER_DATA["date"])
        order_page.select_rental_period(TOP_ORDER_DATA["period"])
        order_page.select_black_color()
        order_page.fill_comment(TOP_ORDER_DATA["comment"])
        order_page.click_order_button()
        order_page.confirm_order()
        assert order_page.is_order_created()

    @allure.title("Проверка нижней кнопки")
    def test_order_button_button(self, main_page, order_page):
        main_page.open()
        main_page.confirm_click_if_present()
        main_page.order_bottom_click()

        order_page.fill_name(BOTTOM_ORDER_DATA["name"])
        order_page.fill_last_name(BOTTOM_ORDER_DATA["last_name"])
        order_page.fill_address(BOTTOM_ORDER_DATA["address"])
        order_page.select_metro(BOTTOM_ORDER_DATA["metro"])
        order_page.fill_phone(BOTTOM_ORDER_DATA["phone"])
        order_page.next_button_click()

        order_page.fill_date(BOTTOM_ORDER_DATA["date"])
        order_page.select_rental_period(BOTTOM_ORDER_DATA["period"])
        order_page.select_black_color()
        order_page.fill_comment(BOTTOM_ORDER_DATA["comment"])
        order_page.click_order_button()
        order_page.confirm_order()
        assert order_page.is_order_created()

    @allure.title("Проверка самоката")
    def test_scooter_logo(self, main_page):
        main_page.open()
        main_page.scooter_logo_click()
        assert main_page.is_current_url(main_page.URL)

    @allure.title("Проверка лого яндекса")
    def test_yandex_logo(self, main_page):
        main_page.open()
        main_page.open_yandex()
        assert main_page.is_url_contains("ya.ru")
                  

