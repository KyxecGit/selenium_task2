from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ResultPage(BasePage):
    DROPDOWN = (By.ID, "sort_by_trigger")
    SORT_BY_PRICE = (By.ID, "Price_DESC")
    GAME_LIST = (By.CSS_SELECTOR, ".search_result_row")
    PRICE = (By.XPATH, "(//div[contains(@class, 'discount_final_price')])[1]")

    def price_filter(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN))
        dropdown.click()
        price_sort = self.wait.until(EC.element_to_be_clickable(self.SORT_BY_PRICE))
        price_sort.click()

    def game_count(self):
        games = self.wait.until(EC.presence_of_all_elements_located(self.GAME_LIST))
        return len(games)

    def get_first_game_price(self):
        first_price_element = self.wait.until(EC.presence_of_element_located(self.PRICE))
        price_text = first_price_element.text
        price_text = price_text.split("\n")[-1]
        price_text = price_text.replace("USD", "").replace("$", "").replace(",", ".").strip()
        return float(price_text)

    def wait_for_price_change(self, old_price):
        self.wait.until(lambda driver: self.get_first_game_price() != old_price)
