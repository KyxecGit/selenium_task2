from selenium.webdriver.support.ui import WebDriverWait
from utils.config_reader import ConfigReader
from utils.browser import Browser

# Загружаем тайм-аут из конфигурации
timeout = ConfigReader('timeout')

class BasePage:
    """
    Базовый класс для страниц сайта.
    """

    def __init__(self):
        """
        Инициализируем WebDriver и WebDriverWait.
        """
        self.driver = Browser.get_driver()  # Получаем WebDriver
        self.wait = WebDriverWait(self.driver, timeout)  # Устанавливаем WebDriverWait с тайм-аутом
