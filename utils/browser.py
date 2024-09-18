from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:
    _instance = None

    @staticmethod
    def get_driver(language='en'):
        if Browser._instance is None:
            chrome_options = Options()
            chrome_options.add_argument(f'--lang={language}')
            Browser._instance = webdriver.Chrome(options=chrome_options)
        return Browser._instance

    @staticmethod
    def quit_driver():
        if Browser._instance:
            Browser._instance.quit()
            Browser._instance = None
