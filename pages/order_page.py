from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys



class OrderPage:
    URL = "https://qa-scooter.education-services.ru/order"

    def get_header_text(self):
        return self.driver.find_element(*OrderPageLocators.HEADER).text

    def __init__(self, driver):
            self.driver = driver

    def fill_name(self, name):
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                               element_to_be_clickable(OrderPageLocators.NAME)).send_keys(name)

    def fill_last_name(self, last_name):
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                                   element_to_be_clickable(OrderPageLocators.LAST_NAME)).send_keys(last_name)

    def fill_address(self, address):
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                                   element_to_be_clickable(OrderPageLocators.ADDRESS)).send_keys(address)
    
    def fill_phone(self, phone):
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                                   element_to_be_clickable(OrderPageLocators.PHONE)).send_keys(phone)

    def next_button_click(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                                           element_to_be_clickable(OrderPageLocators.NEXT_BUTTON)).click()

    def select_metro(self, station):
        WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(
            OrderPageLocators.METRO
            )
        ).send_keys(station)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                OrderPageLocators.metro_option(station)
            )
        ).click()

    def fill_date(self, date):
        date_field = self.driver.find_element(*OrderPageLocators.DATE)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ESCAPE)

    def select_rental_period(self, period):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        self.driver.find_element(*OrderPageLocators.rental_period_option(period)).click()


    def select_black_color(self):
        self.driver.find_element(*OrderPageLocators.BLACK_COLOR).click()

    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def confirm_order(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    def is_order_created(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                OrderPageLocators.ORDER_CREATED)).is_displayed()
