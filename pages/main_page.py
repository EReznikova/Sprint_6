from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    URL = "https://qa-scooter.education-services.ru/"

    def confirm_click(self):
        self.element_click(MainPageLocators.CONFIRM_BUTTON)

    def confirm_click_if_present(self):
        self.click_if_present(MainPageLocators.CONFIRM_BUTTON)

    def yandex_logo_click(self):
        self.element_click(MainPageLocators.YANDEX_LOGO)

    def open_yandex(self):
        original_window = self.get_current_window()
        self.yandex_logo_click()
        self.switch_to_new_window(original_window)
        self.wait_for_url_contains("ya.ru")

    def scooter_logo_click(self):
        self.element_click(MainPageLocators.SCOOTER_LOGO)

    def click_accordion_button(self, number):
        locator = MainPageLocators.accordion_button(number)
        self.scroll_and_click(locator)

    def get_accordion_panel_text(self, number):
        return self.get_element_text(MainPageLocators.accordion_panel(number))

    def order_top_click(self):
        self.element_click(MainPageLocators.ORDER_TOP_BUTTON)

    def order_bottom_click(self):
        self.element_click(MainPageLocators.ORDER_BOTTOM_BUTTON)

