from configparser import ConfigParser
import os


def read_configuration(category, key):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(current_dir, '..', 'configuration', 'config.ini')

    config = ConfigParser()
    config.read(config_path)
    return config.get(category, key)

