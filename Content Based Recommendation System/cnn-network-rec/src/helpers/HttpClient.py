from src.Lib.libraries import *


def get_data_url(url):

    """
    Fetch data from a given URL and return the JSON response if successful.
    
    The function performs the following steps:
    1. Sends a GET request to the specified URL.
    2. Checks the HTTP status code to ensure the request was successful.
    3. Parses the response as JSON.
    4. Checks if the 'success' key in the JSON response is True.
    5. Returns the JSON data if the request was successful, otherwise prints an error message.

    Parameters:
    url (str): The URL to fetch data from.

    Returns:
    dict or None: The JSON data if the request is successful and 'success' is True, 
                  otherwise None if the request fails or 'success' is False.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for bad status codes
        data = response.json()
        if data["success"] == True:
            return data
        else:
            print("Request was not successful.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data from the URL: {e}")
        return None
                


def get_image_url(url, path, id):

    """
    Parameters:
    url (str): The base URL to which the path will be appended.
    path (str): The path to append to the base URL.
    id (str): The product ID for logging purposes.

    Returns:
    bytes: The content of the image if successfully retrieved.
    None: If the image could not be retrieved after the maximum number of retries or an error occurs.
    
    """
    final_url = f"{url}{path}"
    print("Final URL:", final_url)

    try:
        retries = 0
        while retries < 2:
            response = requests.get(final_url, headers={'User-Agent': 'Mozilla/5.0'})

            if response.status_code == 200:
                print("response:", response)
                return response.content
            else:
                print(f"Failed to download image for product_id: {id} - Status code {response.status_code}")
                retries += 1
        print(f"Failed to download image for product_id: {id} - Max retries exceeded")
        return None
    except Exception as e:
        print(f"Error downloading image for product_id: {id} - {e}")
        return None