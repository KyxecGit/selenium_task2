import pytest
from pages.home_page import HomePage
from pages.result_page import ResultPage
from utils.config_reader import ConfigReader

# Загружаем тестовые данные из конфигурационного файла
test_data = ConfigReader('test_data')

@pytest.mark.parametrize("game, min_count", test_data)
def test_game_search(browser, game, min_count):
    """
    Проверяет функциональность поиска игр и фильтрации по цене.

    Параметры:
        browser (WebDriver): Экземпляр WebDriver, предоставленный фикстурой.
        game (str): Название игры для поиска.
        min_count (int): Минимальное количество игр, которое должно быть найдено после фильтрации.

    Проверяет:
        Количество игр после применения фильтра по цене больше минимального количества.
    """
    home_page = HomePage()  # Создаем объект страницы поиска
    result_page = ResultPage()  # Создаем объект страницы результатов

    home_page.search_game(game)  # Ищем игру
    result_page.price_filter()  # Применяем фильтр по цене

    game_count = result_page.game_count()  # Получаем количество найденных игр

    assert game_count > min_count  # Проверяем, что найденное количество игр больше минимального
