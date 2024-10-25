import requests
from src.helpers.Config import get_config
from src.helpers.Logger import get_logger
import json

logger = get_logger(__name__)


def fetch_api_status(base_url,endpoint):
  

  """ 
    Fetch the status from a given API endpoint and return the data if successful.
    
    Parameters:
    base_url (str): The base URL of the API.
    endpoint (str): The specific endpoint of the API to fetch data from.
    
    Returns:
    dict or None: Returns the data in JSON format if the request is successful (HTTP status code 200).
                  Returns None if there is an error or the status code is not 200.
  """
  url = base_url + endpoint

  try:
     response = requests.get(url)

     if response.status_code == 200:
      data = response.json()  

      logger.info("Data fetched successfully")
      return data
     else:
      logger.warning(f'n error occurred {response.status_code}')
  except Exception as error:
        logger.error(f'fetch_api_status {error}')

  return None



def request(url='',type='GET',payload = {} ,headers = {}):
    '''
    Make an HTTP request to the specified URL with the given parameters.
    
    Parameters:
    url (str): The URL to send the request to.
    type (str): The HTTP method to use for the request (e.g., 'GET', 'POST'). Default is 'GET'.
    payload (dict): The payload to include in the request. Default is an empty dictionary.
    headers (dict): The headers to include in the request. Default is an empty dictionary.
    
    Returns:
    dict: The response data parsed as a JSON object.
    '''
    response = requests.request("GET", url, headers=headers, data=payload)
    json.loads(response.text)
