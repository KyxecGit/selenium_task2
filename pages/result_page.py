from selenium.webdriver.common.by import By
from .base_page import BasePage

class ResultPage(BasePage):
    DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_BY_PRICE = (By.ID, "Price_DESC")
    GAME_LIST = (By.CSS_SELECTOR, ".search_result_row")

    def price_filter(self):
        """
        Применяет сортировку по цене (по убыванию).
        """
        self.wait_and_click(*self.DROPDOWN)
        self.wait_and_click(*self.SORT_BY_PRICE)

    def game_count(self):
        """
        Считает количество игр на странице результатов.
        """
        games = self.get_elements(self.GAME_LIST)
        return len(games)
