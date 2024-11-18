
from helper.libraries import *




def upload(api_url, tags_list):
    """
    Sends a list of tags to the InsertGeminiTags API.

    :param api_url: str: The API URL endpoint.
    :param tags_list: list: The list of tags to send.
    :return: dict: The response from the API.
    """
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        # Send the list of dictionaries (tags_list) as JSON in the POST request
        response = requests.post(api_url, json=tags_list, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print({"status": "success", "data": response.json()})
            return {"status": "success", "data": response.json()}
        else:
            print({"status": "fail", "code": response.status_code})
            return {"status": "fail", "code": response.status_code}
    except Exception as e:
        print({"status": "error", "message": str(e)})
        return {"status": "error", "message": str(e)}
