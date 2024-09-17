from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ResultPage(BasePage):
    """
    Класс для страницы результатов поиска.
    """

    DROPDOWN = (By.ID, "sort_by_trigger")  # Локатор для выпадающего списка сортировки
    SORT_BY_PRICE = (By.ID, "Price_DESC")  # Локатор для сортировки по цене
    GAME_LIST = (By.CSS_SELECTOR, ".search_result_row")  # Локатор для списка игр

    def price_filter(self):
        """
        Применяет фильтр по цене.
        """
        dropdown = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN))  # Ожидаем доступности выпадающего списка
        dropdown.click()  # Открываем выпадающий список

        price_sort = self.wait.until(EC.element_to_be_clickable(self.SORT_BY_PRICE))  # Ожидаем доступности элемента сортировки
        price_sort.click()  # Выбираем сортировку по цене

    def game_count(self):
        """
        Возвращает количество найденных игр.
        
        Возвращает:
            int: Количество игр в списке.
        """
        games = self.wait.until(EC.presence_of_all_elements_located(self.GAME_LIST))  # Ожидаем загрузки всех элементов
        return len(games)  # Возвращаем количество игр
