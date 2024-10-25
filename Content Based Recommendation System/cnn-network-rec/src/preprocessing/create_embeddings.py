from .Extract_feature import *
from src.Lib.libraries import *
from src.helpers.HttpClient import *
from src.preprocessing.download_image import *

def create_embed(data, images_folder, model, request_image_url):

    """
    Generate embeddings for images specified in the input data and save the results in a DataFrame.

    This function processes a given dataset containing product IDs and image URLs. It downloads the images,
    extracts embeddings using the provided model, and stores the results in a DataFrame.

    Parameters:
    data (dict): A dictionary containing image URLs and product IDs.
    images_folder (str): The folder path where images will be saved temporarily.
    model (keras.Model): A pre-trained model used to extract image embeddings.
    request_image_url (str): The base URL to be used for image requests.

    Returns:
    tuple:
        - embeddings (numpy.ndarray): A NumPy array containing the embeddings for each image.
        - df_embedding (pandas.DataFrame): A DataFrame with columns 'product_id' and 'embedding', containing the product IDs and their corresponding embeddings.
    """
    try:
        # Create a DataFrame to store file names, product IDs, and embeddings
        if data is not None :
            df_embedding = pd.DataFrame(columns=['product_id', 'embedding'])
            results = data["result"]
            for item in results:
                product_id = item["product_id"]
                file_link = item["image"]
                print(f"Product ID: {product_id} #-----# Image: {file_link}")
                logging.info(f"Product ID: {product_id} #-----# Image: {file_link}")
                # base_path = file_link.rsplit(".", 1)[0]
                url_response = get_image_url(request_image_url, file_link, product_id)
                if url_response is not None:
                    # Download_images(file_link, image_save_path=images_folder, url=request_image_url)
                    Download_images(file_link, images_folder, url_response)
                    file_path = os.path.join(images_folder, str(file_link))
                    # Extract features from the image
                    embedding = extract_features(file_path, model)
                    # os.remove(file_path)

                    # Append the filename, product ID, and embedding to the new DataFrame
                    if embedding is not None:
                        df_embedding = df_embedding._append({'product_id': product_id, 'embedding': embedding},
                                                        ignore_index=True)
                else : 
                    logging.error("---- url_response is None  ----")
                    print("---- url_response is None   ----")
                # df_embedding.to_csv("embeddings.csv")
            embeddings = np.array(df_embedding['embedding'].tolist())
            logging.info("---- image Embedding csv file created ----")
        else :
            logging.error("---- Request data is None  ----")
            print("---- Request data is None  ----")
    except Exception as e:
        logging.error(f"An error occurred in Create_embedding function : {e}")
        embeddings = None
        df_embedding = None

    return embeddings, df_embedding