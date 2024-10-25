
from src.helpers.Logger import get_logger
from src.helpers.Config import *
import requests
import os 
from datetime import date

logger = get_logger(__name__)

def upload():
    """
    The `upload` function reads a CSV file, prepares the file path, uploads the file to a specified URL
    using a POST request, and logs the process.
    """
    try : 
            
        logger.info('cosin csv started reading')  
        BASE_PATH=os.getcwd()
        env = get_config('env', 'env')

        cosin_path=os.path.join(BASE_PATH,'cosin_similarity_csv').replace('\\', '/')
        cosin_save_path = f"{cosin_path}/cosine_similarity_{env}_TFIDF.csv"

        logger.info('Uploading file')  


        url = 'https://dev-api.fashionpass.com/api/v1/Content/UploadFiles'
        files = {'file': open(cosin_save_path, 'rb')}
        data = {'folder': 'ml_csv_experiment'}

        try:

            response = requests.post(url, files=files, data=data)

            print(response.text)
            logger.info('file uploaded')
            print(f"uploaded csv {data}")

            logger.info(response.text)  
        except : 
                logger.error("Error in Upload Function")


    except : 
        logger.error("Error in Upload Function")
