from src.helpers.Config import *
from src.Lib.libraries import *
from src.preprocessing.csv import *
import requests
import os 
from datetime import date
import logging

def upload(csv_save_path,env):
    """
    Upload a CSV file to a remote server.

    This function uploads a CSV file to a specified URL endpoint using a POST request.
    It logs the process and handles errors gracefully.

    Parameters:
    csv_save_path (str): The local file path of the CSV file to upload.
    env (str): The environment identifier to dev or live.
    """
    try : 
        csv_path = f"cosine_similarity_{env}_CNN.csv"
        csv_save_path = os.path.join(csv_save_path,csv_path)
        logging.info('cosin csv started reading')  

        logging.info('Uploading file')  


        url = 'https://dev-api.fashionpass.com/api/v1/Content/UploadFiles'
        files = {'file': open(csv_save_path, 'rb')}
        data = {'folder': 'ml_csv_experiment'}

        try:

            response = requests.post(url, files=files, data=data)

            print(response.text)
            logging.info('file uploaded')
            
            logging.info(response.text)  
        except : 
                logging.error("Error in Upload Function")


    except : 
        logging.error("Error in Upload Function")
