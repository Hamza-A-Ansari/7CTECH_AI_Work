from helper.libraries import *


def config_file():
    # API to get config.ini from s3
    config_api = ''
    
    # Make a GET request to the API to get the config.ini content
    response = requests.get(config_api)
    # Check if the request was successful
    if response.status_code == 200:
        # Get the content of the response
        config_content = response.text
        
        # Save the config content to a file
        with open('config.ini', 'w') as configfile:
            configfile.write(config_content)
    else:
        raise Exception(f"Failed to download config file. Status code: {response.status_code}")

    # Initialize ConfigParser and read the saved config file
    config = configparser.ConfigParser()
    config_file_path = glob.glob('*config.ini')
    
    if config_file_path:
        config.read(config_file_path[0])
    else:
        raise FileNotFoundError("Config file not found.")
    
    return config

def get_config(region, setting):
    config = config_file()
    return config[region][setting]