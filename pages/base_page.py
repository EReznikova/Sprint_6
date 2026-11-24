from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def element_click(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self, original_window):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.number_of_windows_to_be(2)
        )
        new_window = next(
            window
            for window in self.driver.window_handles
            if window != original_window
        )
        self.driver.switch_to.window(new_window)

    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(text)
        )

    def is_current_url(self, url):
        return self.driver.current_url == url

    def is_url_contains(self, text):
        return text in self.driver.current_url

    def click_if_present(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements and elements[0].is_displayed():
            elements[0].click()
            return True
        return False

    def scroll_and_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({block: 'center'});
            arguments[0].click();
            """,
            element,
        )

    def get_element_text(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator)).text

    def fill_element(self, locator, name):
        WebDriverWait(self.driver, 3).until(expected_conditions.
                                               element_to_be_clickable(locator)).send_keys(name)

    def fill_element_and_press_key(self, locator, text, key):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        element.send_keys(text)
        element.send_keys(key)

    def go_back(self):
        self.driver.back()

    def if_element_visible(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(
                locator)).is_displayed()
