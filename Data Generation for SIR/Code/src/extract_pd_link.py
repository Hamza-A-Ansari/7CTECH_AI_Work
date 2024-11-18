from helper.libraries import *
from helper.HttpClient import *


def fetch_and_filter_image_link(image_endpoint_api):
    try:
        
        # Fetch data from the API
        image_link_data = fetch_api_data(image_endpoint_api)

        # Extract the relevant data
        image_data = image_link_data['result']
        image_data = [(item['product_id'], item['image']) for item in image_data]

        # Create a DataFrame
        image_df = pd.DataFrame(image_data, columns=['product_id', 'product_link'])

        # Filter the DataFrame based on specific file extensions
        valid_extensions = ("1.jpg", "1.jpeg", "1.webp", "1.png")
        image_df = image_df[image_df['product_link'].str.endswith(valid_extensions)]

        # Ensure 'product_id' is of type int
        image_df['product_id'] = image_df['product_id'].astype(int)

        return image_df

    except Exception as e:
        logging.error(f"An error occurred while fetching and filtering image data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
