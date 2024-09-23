import json


class ConfigReader:
    PATH = "data/config.json"
    TEST_DATA_PATH = "data/test_data.json"
    _config_data = None
    _test_data = None

    @staticmethod
    def get_value(key):
        if ConfigReader._config_data is None:
            with open(ConfigReader.PATH) as file:
                ConfigReader._config_data = json.load(file)
        return ConfigReader._config_data.get(key)
    

    @staticmethod
    def get_test_data():
        if ConfigReader._test_data is None:
            with open(ConfigReader.TEST_DATA_PATH) as file:
                ConfigReader._test_data = json.load(file).get('test_data', [])
        return ConfigReader._test_data
