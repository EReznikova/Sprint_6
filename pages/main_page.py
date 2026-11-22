from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from locators.main_page_locators import MainPageLocators


class MainPage:
    URL = "https://qa-scooter.education-services.ru/"

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                            element_to_be_clickable(MainPageLocators.CONFIRM_BUTTON)).click()

    def yandex_logo_click(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.YANDEX_LOGO
            )
        ).click()

    def scooter_logo_click(self):
            self.driver.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    def __init__(self, driver):
        self.driver = driver

    def go_back(self):
        self.driver.back()

    def click_accordion_button(self, number):
        locator = MainPageLocators.accordion_button(number)

        button = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({block: 'center'});
            arguments[0].click();
            """,
            button,
        )    

    def get_accordion_panel_text(self, number):
        panel = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.accordion_panel(number)
            )
        )
        return panel.text

    def order_top_click(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.
                                                    element_to_be_clickable(MainPageLocators.ORDER_TOP_BUTTON)).click()

    def order_bottom_click(self):
        self.driver.find_element(*MainPageLocators.ORDER_BOTTOM_BUTTON).click()   

        