from src.helper.HttpClient import fetch_api_data, thread_download, fetch_csv
from src.preprocessing.prompt import final_prompt
from src.prediction.prediction import prediction
from src.helper.Logger import get_logger
from src.helper.Config import config_file, get_config
from src.transformation.transformation import dataframe
from src.lib.Liabraries import *
from src.preprocessing.load_image import * 
from model.cosine import cosine_model
from model.gemini import gemini_model

logger = get_logger(__name__)

def final_prediction(cat_df ,review_image, log_key):

    log_key += "phase three "
    log_key += "func final prediction"
    logger.info(f"{log_key}")
    
    try:

        try:
            prod_images_dir = get_config('directories', 'images_dir')
            if not os.path.exists(prod_images_dir):
                os.makedirs(prod_images_dir)
                logger.info(f'{log_key} created folder {prod_images_dir}')
        except:
            logger.info(f'{log_key} folder exists ', prod_images_dir)

        # All product image dataframe
        image_endpoint_api = get_config('api', 'product_link_api')
        image_endpoint_data = fetch_api_data(image_endpoint_api,log_key)
        
        image_data = image_endpoint_data['result']
        image_data = [(item['product_id'], item['image']) for item in image_data]
        image_df = dataframe(image_data, ['product_id', 'product_link'])

        image_df = image_df[image_df['product_link'].str.endswith(("1.jpg", "1.jpeg", "1.webp", "1.png"))]
        image_df['product_id'] = image_df['product_id'].astype(int)
        
        df_tag = fetch_csv(get_config('api', 'tags_api'))

        results = []
        incr = 10000
        for _ , row in cat_df.iterrows():
            try : 
                tags = str(row['tag_string'])
                category = str(row['Category'])

                logger.info(f'{log_key} category {category}')
                logger.info(f'{log_key} tags {tags}')

                # Match Product Part
                pp_category = category.replace("&","and").lower()
                df_tag = df_tag.dropna(subset=['tag_string'])
                match_prod_df = df_tag[df_tag['tag_string'].str.contains(pp_category, case=False)]

                # concat part
                new_row = {'product_id': incr, 'tag_string': tags}
                incr += 1
                concat_df = pd.concat([pd.DataFrame(new_row, index=[0]), match_prod_df]).reset_index(drop=True)

                # Cosine similarity part
                cos_df = cosine_model(concat_df,log_key)
                # Top product link part
                cos_df = cos_df.head(80)
                cos_df = cos_df.reset_index(drop=True)

                cos_df['product_id'] = cos_df['product_id'].astype(int)
                top_prod_link_df = pd.merge(cos_df[['product_id']], image_df, on='product_id')
                ids = cos_df['product_id'].to_list()
                # Download images part
                all_images_name_list = os.listdir(prod_images_dir)
                thread_download(top_prod_link_df, prod_images_dir, all_images_name_list,log_key)
            
                image_paths = generate_paths(prod_images_dir, ids)
                existing_files = check_files_exist(image_paths,log_key)

                if len(existing_files) >= 50:
                    all_img = existing_files[:50]
                else:
                    all_img = existing_files 

                images = load_images(all_img,review_image,log_key)  # Loading only the first 80 images
                config = config_file()
                logger.info(f"{log_key} image uploaded {len(all_img)}")
                api_keys = [value for _, value in config.items("gemini_api_key")]

                for api_key in api_keys: 
                    try : 
                        system_instruction = "Your task is to identify the product in the product images that 100 percent  matches the clothing worn in the review image. Provide the ID of the matching product. If no product image matches the review image, return an ID of 0."
                        model = gemini_model(api_key=api_key, system_information=system_instruction, log_key=log_key)
                        chat_session = model.start_chat(
                                history=[
                                    {
                                        "role": "user",
                                        "parts":images
                                    }
                                ]
                            )

                        response = chat_session.send_message(final_prompt(category,tags))

                        response.resolve()

                        resultant_id = response.text
                        numeric_value = ''.join(filter(str.isdigit, resultant_id))

                        results.append(numeric_value)

                        break

                    except Exception as e:
                        logger.error(f"{log_key} api key {api_key} error {e}")
                        if api_key == api_keys[-1]:
                            raise
                            
                        continue
            

            except Exception as e:
                logger.error(f"{log_key} loop error {e}")
            
        try:
            results_list = []
            for item in results:
                numbers = re.findall(r'\d+', item)
                results_list.extend(map(int, numbers))

            results_list = [str(x) if not isinstance(x, str) else x for x in results_list]

        except Exception as e:
            logger.info(f"{log_key} error in extracting product id {e}")
            results_list = [0]

        logger.info(f"{log_key} results {results_list}")
        return results_list
    
    except Exception as e:
        logger.error(f"{log_key} error {e}")
        return [0]