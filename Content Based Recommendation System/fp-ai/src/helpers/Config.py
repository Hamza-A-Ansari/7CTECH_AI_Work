import configparser
import glob


config = configparser.ConfigParser()
config_file = glob.glob('*config.ini')
print("config.ini file readed : " , config_file)
config.read(config_file)

def get_config(region, setting):
    return config[region][setting]

