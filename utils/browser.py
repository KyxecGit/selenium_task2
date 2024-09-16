from selenium import webdriver

class Browser:
    _instance = None

    @staticmethod
    def get_driver():
        """
        Возвращает единственный экземпляр WebDriver (Singleton).
        """
        if Browser._instance is None:
            Browser._instance = webdriver.Chrome()
        return Browser._instance
