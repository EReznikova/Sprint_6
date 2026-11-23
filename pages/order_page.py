from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    URL = "https://qa-scooter.education-services.ru/order"

    def get_header_text(self):
        return self.get_element_text(OrderPageLocators.HEADER)

    def fill_name(self, name):
        self.fill_element(OrderPageLocators.NAME, name)

    def fill_last_name(self, last_name):
        self.fill_element(OrderPageLocators.LAST_NAME, last_name)

    def fill_address(self, address):
        self.fill_element(OrderPageLocators.ADDRESS, address)

    def fill_phone(self, phone):
        self.fill_element(OrderPageLocators.PHONE, phone)

    def next_button_click(self):
        self.element_click(OrderPageLocators.NEXT_BUTTON)

    def select_metro(self, station):
        self.fill_element(OrderPageLocators.METRO, station)
        self.element_click(OrderPageLocators.metro_option(station))

    def fill_date(self, date):
        self.fill_element_and_press_key(
            OrderPageLocators.DATE,
            date,
            Keys.ESCAPE,
        )

    def select_rental_period(self, period):
        self.element_click(OrderPageLocators.RENTAL_PERIOD)
        self.element_click(OrderPageLocators.rental_period_option(period))


    def select_black_color(self):
        self.element_click(OrderPageLocators.BLACK_COLOR)

    def fill_comment(self, comment):
        self.fill_element(OrderPageLocators.COMMENT, comment)

    def click_order_button(self):
        self.element_click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.element_click(OrderPageLocators.YES_BUTTON)

    def is_order_created(self):
        return self.if_element_visible(OrderPageLocators.ORDER_CREATED)
