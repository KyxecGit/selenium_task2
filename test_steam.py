import logging
from pages.home_page import HomePage
from pages.result_page import ResultPage

logging.basicConfig(level=logging.INFO)

def test_game_search(setup_browser, language, game_name, min_count):
    """
    Тест на поиск игры и проверку количества результатов после применения фильтра.
    """
    home_page = HomePage()
    result_page = ResultPage()

    logging.info(f"Поиск игры: {game_name}")
    home_page.search_game(game_name)

    logging.info("Применение фильтра по цене")
    result_page.price_filter()

    logging.info("Подсчет количества игр")
    game_count = result_page.game_count()

    logging.info(f"Количество игр: {game_count}, Минимум ожидалось: {min_count}")
    assert game_count > min_count, f"Ожидалось минимум {min_count} игр, но найдено только {game_count}."
