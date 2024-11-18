from helper.libraries import *
from prompt import *



def create_model(api_key):
    try:
        genai.configure(api_key=api_key)
        generation_config = {
            "temperature": 0,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "application/json",
        }
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            safety_settings=safety_settings,
            generation_config=generation_config,
            system_instruction="""Please provide answers only from the tag listed. If no answer is applicable, respond with "null". Ensure that all answers are in JSON format.
            example response : 
            {"product-category":[], sub-category":[], "color":[],"color style":[], "multicolor":[], "material": [],"pattern": [],"sleeve style": [],"shoulder_style":[],"strap_style" : [],"neck_style":[] ,"special features or embellishments": []}",
"""
        )
        return model
    except Exception as e:
        logging.error(f"Error creating model with API key {api_key}: {e}")
        raise


def csv_file_exists(csv_file_path):
    exists = os.path.isfile(csv_file_path)
    return exists



def process_and_append_data(data, product_id, csv_file_path):
    try:
        # Dynamically process the data dictionary
        data_processed = {"product_id": [product_id]}
        
        for key, value in data.items():
            # Ensure that the key exists in the data dictionary
            if isinstance(value, list):
                data_processed[key] = [",".join(value)]
            else:
                data_processed[key] = [value]

        df_new = pd.DataFrame(data_processed)

        # Clean up the new data
        df_new.fillna('', inplace=True)

        df_new['tag_string'] = df_new.iloc[:, 1:].apply(lambda x: ' '.join(x), axis=1)
        df_new['tag_string'] = df_new['tag_string'].str.lower()
        df_new['tag_string'] = df_new['tag_string'].replace('and ', ' ', regex=True)
        df_new['tag_string'] = df_new['tag_string'].replace('null', ' ', regex=True)
        df_new['tag_string'] = df_new['tag_string'].replace('none', ' ', regex=True)
        df_new['tag_string'] = df_new['tag_string'].str.replace(',+', ' ', regex=True).str.strip()
        df_new['tag_string'] = df_new['tag_string'].str.replace(r'[\"\[\]]', '', regex=True)
        df_new['tag_string'] = df_new['tag_string'].str.replace(r'\s+', ' ', regex=True)
        df_new = df_new[["product_id", 'tag_string']]
        df_new = df_new[df_new['tag_string'] != '']

        # Check if the file exists and read the existing data
        if csv_file_exists(csv_file_path):
            df_existing = pd.read_csv(csv_file_path)
        else:
            df_existing = pd.DataFrame(columns=["product_id", "tag_string"])

        # Append new data to the existing data
        df_complete = df_existing._append(df_new, ignore_index=True)

        # Save the combined data back to the CSV file
        df_complete.to_csv(csv_file_path, index=False)

        logging.info(f"Data appended successfully for product_id: {product_id}.")
        
        return df_complete

    except Exception as e:
        logging.error(f"Error processing data for product_id {product_id}: {e}")
        raise  # Re-raise the exception after logging it





def log_error(product_id, error_csv_file_path="error_images.csv"):
    try:

        with open(error_csv_file_path, "a", newline='') as error_csv_file:
            error_csv_writer = csv.writer(error_csv_file)
            error_csv_writer.writerow([product_id])

        logging.info(f"Logged error for product ID: {product_id}.")
    
    except Exception as e:
        logging.error(f"Error logging error for product ID {product_id}: {e}")
        raise



def process_images(image_path,image_id, api_keys,category , tag_collection_csv_path="tag_collection_clothing.csv", error_csv_file_path="error_images.csv"):
    try:
        
        image =  Image.open(image_path)
        if image.mode == 'P':
            image = image.convert('RGB')
        for _ ,api_key in api_keys :
            try  :     
                model = create_model(api_key)

                response = model.generate_content([prompt(category), image], request_options={"timeout": 10})
                response.resolve()
                break
            except Exception as e:
                logging.warning(f"Error processing image for ID {id} with API key {api_key}: {e}")
        logger.info(response.text)
        data = json.loads(response.text)
        os.remove(image_path)
            
        logging.info(f"Data generated for {image_id}.")
        append_data = process_and_append_data(data, image_id, tag_collection_csv_path)
        return append_data
    except Exception as e:
        logging.error(f"Error in process_images function: {e}")
        raise



def get_cat_by_id(data, target_item1):
    result = [item['product_category'] for item in data if item['product_id'] == target_item1]
    return result[0] if result else None  # Return first match or None if not found


def format_product_data(df):
    # Initialize an empty list to store formatted dictionaries
    formatted_data = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        product_id = row['product_id']  # Remove any extra spaces
        tag_string = row['tag_string'].strip()  # Remove any extra spaces
        
        # Create a dictionary with the required keys and append it to the list
        formatted_data.append({
            "product_id": product_id,
            "tag_string": tag_string
        })
        

    # Return  formatted data as a list of dictionaries
    return formatted_data