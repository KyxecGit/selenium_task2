import json


class ConfigReader:
    PATH = "data/config.json"
    _config_data = None

    @staticmethod
    def get_value(key):
        if ConfigReader._config_data is None:
            with open(ConfigReader.PATH) as file:
                ConfigReader._config_data = json.load(file)
        return ConfigReader._config_data.get(key)
