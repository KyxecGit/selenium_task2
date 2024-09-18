import json
import pytest
from pages.home_page import HomePage
from pages.result_page import ResultPage


with open("data/test_data.json") as file:
    data = json.load(file)
    test_data = data['test_data']


@pytest.mark.parametrize("game, min_count", test_data)
def test_game_price_and_count_after_filter(browser, game, min_count):
    home_page = HomePage()
    result_page = ResultPage()

    home_page.search_game(game)
    assert result_page.is_page_loaded(), "Страница результатов не загрузилась"

    price_before_filter = result_page.get_first_game_price()
    result_page.price_filter()
    result_page.wait_for_price_change(price_before_filter)
    price_after_filter = result_page.get_first_game_price()
    assert price_before_filter != price_after_filter, "Цена первой игры не изменилась после применения фильтра"

    game_count = result_page.game_count()
    assert game_count > min_count, f"Ожидалось больше {min_count} игр, но найдено {game_count} для '{game}'"
