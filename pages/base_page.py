from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import Browser
from utils.config_reader import ConfigReader

config = ConfigReader('data/config.json')
timeouts = config.get("timeouts")

class BasePage:
    def __init__(self):
        self.driver = Browser.get_driver()
        self.wait = WebDriverWait(self.driver, timeouts['explicit_wait'])

    def wait_element(self, by, value):
        """
        Ожидает появления элемента на странице.
        """
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_and_click(self, by, value):
        """
        Ожидает, пока элемент станет кликабельным, и кликает по нему.
        """
        element = self.wait_element(by, value)
        self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def type_text(self, by, value, keys):
        """
        Вводит текст в элемент на странице.
        """
        element = self.wait_element(by, value)
        element.send_keys(keys)

    def get_elements(self, locator):
        """
        Возвращает список элементов, найденных по локатору.
        """
        return self.driver.find_elements(*locator)

    def scroll_down(self):
        """
        Прокручивает страницу вниз.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
