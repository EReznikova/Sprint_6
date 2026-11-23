from pages.main_page import MainPage
import pytest
from selenium import webdriver
import allure
from data.faq_data import FAQ_DATA

class TestFAQ:
    @allure.title("FAQ: вопрос {param_id}")
    @pytest.mark.parametrize(
        "number, expected_text",
        FAQ_DATA
    )
    def test_faq(self, faq_page, number, expected_text):
        with allure.step(f"Открыть вопрос {number + 1}"):
            faq_page.click_accordion_button(number)

        with allure.step("Проверить текст ответа"):
            assert faq_page.get_accordion_panel_text(number) == expected_text
