import json

class ConfigReader:
    """
    Класс для чтения значений из конфигурационного файла.
    """

    def __new__(cls, key):
        """
        Создает новый экземпляр класса и возвращает значение по ключу из конфигурационного файла.

        Аргументы:
            key (str): Ключ для поиска значения в конфигурационном файле.

        Возвращает:
            Значение, соответствующее ключу из конфигурационного файла.
        """
        instance = super(ConfigReader, cls).__new__(cls)
        instance.key = key
        instance.value = instance.load_config(key)  # Загружаем значение по ключу
        return instance.value

    def load_config(self, key):
        """
        Загружает значение из конфигурационного файла по заданному ключу.

        Аргументы:
            key (str): Ключ для поиска значения.

        Возвращает:
            Значение из конфигурационного файла.
        """
        with open("data/config.json") as file:
            config = json.load(file)  # Загружаем конфигурацию из файла
        return config.get(key)  # Возвращаем значение по ключу
