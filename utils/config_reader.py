import json

class ConfigReader:
    def __init__(self, config_file):
        """
        Загружает конфигурацию из JSON-файла.
        """
        with open(config_file) as f:
            self.config = json.load(f)

    def get(self, key):
        """
        Получает значение из конфигурации по ключу.
        """
        return self.config.get(key)

    def load_data(self):
        """
        Возвращает полное содержимое конфигурации.
        """
        return self.config
