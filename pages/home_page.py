from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH = (By.ID, "store_nav_search_term")

    def search_game(self, game):
        """
        Выполняет поиск игры по её названию.
        """
        self.type_text(*self.SEARCH, game + Keys.RETURN)
