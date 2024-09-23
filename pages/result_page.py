from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ResultPage(BasePage):
    GAME_LIST = (By.CSS_SELECTOR, ".search_result_row")
    DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_BY_PRICE = (By.ID, "Price_DESC")
    SEARCH_RESULT_CONTAINER = (By.ID, "search_result_container")

    def set_filter_price(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN))
        dropdown.click()
        price_sort = self.wait.until(EC.element_to_be_clickable(self.SORT_BY_PRICE))
        price_sort.click()

    def get_games_count(self):
        games = self.wait.until(EC.presence_of_all_elements_located(self.GAME_LIST))
        return len(games)

    def wait_for_filter_to_apply(self):
        short_wait = WebDriverWait(self.driver, 10, poll_frequency=0.05)
        search_result_container = short_wait.until(EC.presence_of_element_located(self.SEARCH_RESULT_CONTAINER))
        short_wait.until(lambda driver: search_result_container.get_attribute("style") != "")


