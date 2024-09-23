from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    SEARCH = (By.ID, "store_nav_search_term")

    def search_game(self, game):
        element = self.wait.until(EC.visibility_of_element_located(self.SEARCH))
        element.send_keys(game + Keys.RETURN)
