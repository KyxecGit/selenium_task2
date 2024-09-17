from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    """
    Класс для главной страницы сайта.
    """

    SEARCH = (By.ID, "store_nav_search_term")  # Локатор для поля поиска

    def search_game(self, game):
        """
        Выполняет поиск игры.

        Аргументы:
            game (str): Название игры для поиска.
        """
        element = self.wait.until(EC.visibility_of_element_located(self.SEARCH))  # Ожидаем появления элемента
        element.send_keys(game + Keys.RETURN)  # Вводим название игры и отправляем поиск
