from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.CSS_SELECTOR, ".select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    HEADER = (By.CLASS_NAME, 'Order_Header__BZXOb')

    @staticmethod
    def metro_option(station):
        return (
            By.XPATH,
            f"//button[contains(@class, 'select-search__option') "
            f"and normalize-space(.)='{station}']"
        )

    DATE = (By.XPATH,"//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CSS_SELECTOR, ".Dropdown-control")

    @staticmethod
    def rental_period_option(period):
        return (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and text()='{period}']"
        )

    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")
    COMMENT = (By.XPATH,"//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH,"//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_CREATED = (By.XPATH, "//*[text()='Заказ оформлен']")
