from src.lib.Libraries import *


def config_file():
    config = configparser.ConfigParser()
    config_file = glob.glob('*config.ini')
    config.read(config_file)

    return config

def get_config(region, setting):
    config = config_file()
    return config[region][setting]