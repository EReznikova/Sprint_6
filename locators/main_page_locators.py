from selenium.webdriver.common.by import By


class MainPageLocators:
    CONFIRM_BUTTON = [By.ID, "rcc-confirm-button"]
    ORDER_TOP_BUTTON = (
    By.XPATH,
    "//div[contains(@class, 'Header_Nav')]"
    "//button[normalize-space()='Заказать']"
)
    ORDER_BOTTOM_BUTTON = [By.XPATH, "(//button[normalize-space()='Заказать'])[last()]"]
    YANDEX_LOGO = (By.XPATH, "//a[.//img[@alt='Yandex']]")
    SCOOTER_LOGO = (By.XPATH,"//a[.//img[@alt='Scooter']]")

    def accordion_button(number: int):
        return By.ID, f"accordion__heading-{number}"

    def accordion_panel(number: int):
        return By.ID, f"accordion__panel-{number}"    


    