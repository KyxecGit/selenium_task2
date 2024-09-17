from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser:
    """
    Класс для управления единственным экземпляром WebDriver.
    """
    _instance = None  # Хранит единственный экземпляр WebDriver

    @staticmethod
    def get_driver(language='en'):
        """
        Получает экземпляр WebDriver. Создает его, если он не был создан ранее.

        Аргументы:
            language (str): Язык браузера (по умолчанию 'en').

        Возвращает:
            WebDriver: Экземпляр WebDriver.
        """
        if Browser._instance is None:
            chrome_options = Options()
            chrome_options.add_argument(f'--lang={language}')  # Устанавливаем язык браузера
            Browser._instance = webdriver.Chrome(options=chrome_options)  # Создаем экземпляр WebDriver
        return Browser._instance
    
    @staticmethod
    def quit_driver():
        """
        Завершает работу WebDriver и очищает экземпляр.
        """
        if Browser._instance:
            Browser._instance.quit()  # Закрываем WebDriver
            Browser._instance = None  # Очищаем ссылку на экземпляр
