from src.lib.Liabraries import *
from src.helper.Config import get_config
from src.helper.Logger import get_logger

logger = get_logger(__name__)

def fetch_api_data(url,log_key):
    log_key += " func fetch api data"
    try: 
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()  
            logger.info(f'{log_key} product image link fetched')

        return data
    except Exception as e:
        logger.error(f"{log_key} error {e}")

        return None


def fetch_csv(api):
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


# Function to download images
def download_images(row, dir, all_images, log_key):

    # Loop through each image and download it
    image_endpoint = row['product_link']
    product_id = row['product_id']

    image_url = f"{get_config('api', 'fp_images_api')}{image_endpoint}"

    image_name = f"{product_id}.jpg"
    
    image_path =  f"{dir}/{image_name}"

    if image_name not in all_images:
        
        # Image response
        img_response = requests.get(image_url)

        # Check if the response status code is OK (200)
        if img_response.status_code == 200:

            # Download image
            with open(image_path, 'wb') as f:
                f.write(img_response.content)
        else:
            logger.info(f'{log_key} image downloading error {image_url}')


def thread_download(df, dir, all_images, log_key):

    log_key += " func download images"
    num_threads = int(get_config('threading', 'num_threads'))

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for _, row in df.iterrows():
            futures.append(executor.submit(download_images, row, dir, all_images, log_key))
        
        # Optionally wait for all threads to complete (or you can handle exceptions)
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logger.error(f'{log_key} Error occurred: {e}')



# Function to download the image
def instagram_download(endpoint, log_key):

    log_key += " func insta download"

    save_path_insta = get_config('directories', 'insta_dir')
    insta_image_path = f'{save_path_insta}/{endpoint}'
    full_path = f"{get_config('api', 'insta_images_api')}{endpoint}"

    # Create directory if it doesn't exist
    if not os.path.exists(save_path_insta):
        os.makedirs(save_path_insta)
    
    list_dir = os.listdir(save_path_insta)
    if endpoint not in list_dir:
        response = requests.get(full_path)
        if response.status_code == 200:
            with open(insta_image_path, 'wb') as f:
                f.write(response.content)
            logger.info(f'{log_key} image downloaded {insta_image_path}')
        else:
            logger.error(f'{log_key} error downloading insta img {insta_image_path}')

    return insta_image_path