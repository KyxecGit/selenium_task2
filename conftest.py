import pytest
from utils.config_reader import ConfigReader
from utils.browser import Browser

config = ConfigReader('data/config.json')
data = ConfigReader('data/test_data.json')

@pytest.fixture(params=['english', 'russian'])
def language(request):
    """
    Фикстура для получения версии сайта на нужном языке.
    Параметризовано для двух языков: английский и русский.
    """
    yield config.get(f'{request.param}_version')

@pytest.fixture
def setup_browser(language):
    """
    Фикстура для инициализации и закрытия браузера.
    Обнуляет Singleton браузера и открывает сайт на нужном языке.
    """
    Browser._instance = None
    driver = Browser.get_driver()
    driver.get(language)
    yield driver
    driver.quit()

def pytest_generate_tests(metafunc):
    """
    Автоматическая параметризация тестов на основе данных из test_data.json.
    """
    if 'game_name' in metafunc.fixturenames and 'min_count' in metafunc.fixturenames:
        test_data = data.load_data()
        metafunc.parametrize("game_name, min_count", test_data)
