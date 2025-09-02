import configparser


class ConfigReader:

#regular browser config method
    @staticmethod
    def get_config(section: str ,key: str):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config.get(section, key)

#environmental conf method
    @staticmethod
    def get_env(section, key):#get.env method that accepts section(that is in env.ini
        env = configparser.ConfigParser()
        env.read('env.ini')
        return env.get(section, key)


    @staticmethod
    def get_pytest(section, key: str = ""):
        pyt = configparser.ConfigParser()
        pyt.read('pytest.ini')
        return pyt.get(section, key)
