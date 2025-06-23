from src.lib.Libraries import *
from src.helper.Logger import get_logger

logger = get_logger(__name__)


def make_request(url, log_key, params=None, headers=None):
    """
    Makes a GET request to the specified URL with optional parameters and headers.

    Args:
        url (str): The API endpoint.
        log_key (str): The log key to use for logging.
        params (dict, optional): Query parameters for the request.
        headers (dict, optional): Headers for the request.

    Returns:
        dict: Parsed JSON response.

    Raises:
        Exception: If the request fails or the response is invalid.
    """

    log_key += 'make_request '

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"{log_key} Request to {url} failed: {e}")
        return {}
    


def fetch_reviews(product_id, review_url, log_key):
    """
    Fetches reviews for a specific product ID from the second API.

    Args:
        product_id (int): The product ID to fetch reviews for.
        review_url (str): The URL to fetch reviews from.
        log_key (str): The log key to use for logging.

    Returns:
        list[dict]: List of reviews for the product.
        int: Number of reviews for the product.
    """
    log_key += 'fetch_reviews '

    try:
        params = {
            "productid": product_id,
        }
        response = make_request(review_url, log_key, params=params)
        return response.get("reviews", 0)
    
    except Exception as e:
        logger.error(f"{log_key} Request to {review_url} failed: {e}")
        return {}




def dump_data(api_url, data, log_key, headers=None):
    """
    Sends a POST request to add or update review summaries.
    
    Args:
        api_url (str): The API endpoint URL.
        data (list): A list of dictionaries containing product data.
        log_key (str): The log key to use for logging.
        headers (dict, optional): Additional headers for the request.
    
    Returns:
        dict: Contains the status code and response text.
    """
    if headers is None:
        headers = {"Content-Type": "application/json"}

    log_key += 'dump_data'
    try:
        response = requests.post(api_url, headers=headers, json=data)
        
        return {
            "status_code": response.status_code,
            "response_body": response.text
        }

    except Exception as e:
        logger.error(f"{log_key} Request to {api_url} failed: {e}")
        return {}
