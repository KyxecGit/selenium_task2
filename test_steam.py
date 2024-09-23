import pytest
from pages.home_page import HomePage
from pages.result_page import ResultPage
from utils.config_reader import ConfigReader


test_data = ConfigReader.get_test_data()


@pytest.mark.parametrize("game, min_count", test_data)
def test_game_price_and_count_after_filter(browser, game, min_count):
    home_page = HomePage()
    result_page = ResultPage()

    home_page.search_game(game)
    assert result_page.is_page_loaded(), "Страница результатов не загрузилась"

    result_page.set_filter_price()
    result_page.wait_for_filter_to_apply()

    game_count = result_page.get_games_count()
    assert game_count > min_count, f"Ожидалось больше {min_count} игр, но найдено {game_count} для '{game}'"
