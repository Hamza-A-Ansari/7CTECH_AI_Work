import os
import time
import pandas as pd
import logging
from helper.file_exist import *
from helper.HttpClient import *
from src.filter_ids import *
from src.extract_pd_link import *
from helper.Config import *
from helper.libraries import *
from src.image_processor import process_images,log_error,get_cat_by_id,format_product_data
from src.upload import *
config = config_file()

tag_collection_csv_path = "tag_collection_clothing.csv"
# image endpoint df to downlaod images
img_link_df_api = get_config('api', 'product_link_api')
# product_ids and Categories
productids_cat = get_config('api', 'pdid_pdcat')
# Api for donwload tag_collection_clothing csv 
tag_csv_api = get_config('api', 'tag_csv_api')

upload_df_api = get_config('api', 'upload_df_api')

current_directory = os.getcwd()
folder = get_config('directories', 'images_dir')
images_folder = os.path.join(current_directory, folder)


print(images_folder)

if not os.path.exists(images_folder):
    os.makedirs(images_folder)

replacement_dict = {
    'dresses': 'Dresses',
    'jumpsuits': 'Jumpsuits',
    'rompers': 'Rompers',
    'sweatshirts': 'Top',
    'tops': 'Top',
    'sweaters-and-knits': 'Top',
    'jackets-coats-and-blazers': 'Outerwear',
    'jeans-and-denim': 'Pant',
    'skirts': 'Skirts',
    'shorts': 'Skirts',
    'maternity': 'Postpartum',
    'postpartum': 'Postpartum',
    'swimwear': '',
    'activewear-and-loungewear': "",
    'two-piece-set'  : ''

}

def main():
    try:
        logging.info("--------Start main process.---------------")

        complete_tag_data = pd.DataFrame()
        # Fetch product IDs
        data_cat = fetch_api_data(productids_cat)
        all_product_ids  = [item['product_id'] for item in data_cat if 'product_id' in item]
        tag_collection_csv_df =  fetch_tag_csv(tag_csv_api)
        tag_collection_csv_df.to_csv(tag_collection_csv_path, index=False)


        ids = filter_ids_not_in_csv(tag_collection_csv_df, all_product_ids)
        # Fetch and filter image links
        image_url_df = fetch_and_filter_image_link(img_link_df_api)

        # Process images
        if ids:
            try:
                for id in ids:
                    category = get_cat_by_id(data_cat, id)
                    replaced_category  = replacement_dict.get(category, category)

                    logging.info(f"------------{id}---------------")
                    image_url = image_url_df.loc[image_url_df['product_id'] == int(id), 'product_link']
                    print(image_url)
                    if not image_url.empty:
                        image_url = image_url.values[0]
                        logging.info(f"Processing image for ID {id} with URL: {image_url}")

                        ids_path = f"{id}.jpg"
                        image_path = os.path.join(images_folder, ids_path)
                        
                        if csv_file_exists(image_path):
                            logging.info(f"File exists in folder, image read: {image_path}")
                        else:
                            image_url = f"{get_config('api', 'fp_images_api')}{image_url}"
                            download_images(id,image_path, image_url)
                        
                        api_keys = config['api_key'].items()
                        try:
                            complete_tag_data = process_images(image_path, id, api_keys,replaced_category,tag_collection_csv_path=tag_collection_csv_path, error_csv_file_path="error_images.csv")
                            
                            time.sleep(5)

                        except Exception as e:
                            logging.warning(f"Error processing image for ID {id} : {e}")
                            time.sleep(5)  # Retry after a delay

            except Exception as e:
                log_error(id)

        logging.info("All images processed.")

        if not complete_tag_data.empty:
                    df_list = format_product_data(complete_tag_data)
                    upload(upload_df_api, df_list)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
