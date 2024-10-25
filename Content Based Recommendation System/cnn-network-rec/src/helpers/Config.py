from src.Lib.libraries import *


def config():
    try:
        configur = ConfigParser() 
        config_file = glob.glob('*config.ini')
        print("config.ini file readed : " , config_file)
        configur.read(config_file)

        return configur
    except Exception as e:
        print(f"Error loading configuration: {e}")

def get_config(region, setting):
    try:
        configur = config()
        value = configur.get(region, setting)
        return value
    except Exception as e:
        print(f"Error retrieving configuration value: {e}")