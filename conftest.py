import pytest
from utils.browser import Browser
from utils.config_reader import ConfigReader

# Получаем URL и языки из конфигурации
url = ConfigReader('url')
languages = ConfigReader("languages")

@pytest.fixture(params=languages)
def browser(request):
    """
    Фикстура Pytest для создания экземпляра WebDriver.

    Параметры:
        request (FixtureRequest): Объект запроса фикстуры, используется для получения текущего языка.

    Возвращает:
        WebDriver: Экземпляр WebDriver для заданного языка.
    """
    language = request.param  # Получаем язык из параметров фикстуры
    driver = Browser.get_driver(language)  # Получаем WebDriver с заданным языком
    driver.get(url)  # Открываем URL
    yield driver  # Передаем WebDriver в тест
    Browser.quit_driver()  # Закрываем WebDriver после завершения теста
