import pytest
from utils.browser import Browser
from utils.config_reader import ConfigReader


url = ConfigReader.get_value('url')
languages = ConfigReader.get_value("languages")


@pytest.fixture(params=languages)
def browser(request):
    language = request.param
    driver = Browser.get_driver(language)
    driver.get(url)
    yield driver
    Browser.quit_driver()
