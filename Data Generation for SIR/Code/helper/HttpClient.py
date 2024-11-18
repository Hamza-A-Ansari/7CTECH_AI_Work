from helper.libraries import *


def fetch_api_data(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("All product ids df fetched successfully.")
            data = response.json()
            return data
        else:
            logging.error(f"Failed to fetch All product ids df , status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return None


def fetch_tag_csv(api):
    try:
        #Make a GET request to the API to get the CSV content
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            # Convert data to DataFrame
            df = pd.DataFrame(data)

            # Concat tags to create tag string
            df_grouped = df.groupby('product_id')['tag_name'].apply(lambda x: ' '.join(x).lower()).reset_index()
            # Rename the columns
            df_grouped.columns = ['product_id', 'tag_string']

            return df_grouped
        else:
            logger.info(f"API not working: {api}")
    
    except Exception as e:
        logger.error(f"Error in fetch_csv: {e}")
    



def download_images(id,img_save_path, image_url):
    try:
        img_response = requests.get(image_url)

        if img_response.status_code == 200:
            with open(img_save_path, 'wb') as f:
                f.write(img_response.content)
            logging.info(f"{id} Downloaded image - saved {img_save_path}")
        else:
            logging.error(f"Failed to download image {id}from {image_url}, status code: {img_response.status_code}")

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while downloading image {id} from {image_url}: {e}")