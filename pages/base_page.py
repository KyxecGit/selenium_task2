from selenium.webdriver.support.ui import WebDriverWait
from utils.config_reader import ConfigReader
from utils.browser import Browser


timeout = ConfigReader.get_value("timeout")


class BasePage:
    def __init__(self):
        self.driver = Browser.get_driver()
        self.wait = WebDriverWait(self.driver, timeout)

    def is_page_loaded(self):
        return self.driver.execute_script("return document.readyState") == "complete"
        