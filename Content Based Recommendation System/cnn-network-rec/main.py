from src.Lib.libraries import *
from model.model import *
from src.preprocessing.create_embeddings import *
from src.preprocessing.create_cosine import *
from src.helpers.Config import *
from src.preprocessing.download_image import *
from src.helpers.logging import *
from src.helpers.Path import *
from src.preprocessing.upload import *

def main():

    # Create log file
    create_log_file()

    # Reading from Config
    image_save_path = get_config('save_folder','image_folder')
    csv_save_path = get_config('save_folder','csv_folder')
    producte_url_csv = get_config('image_url_data_csv','producte_url_csv')
    request_image_url = get_config('url','request_image_url')
    request_data_url = get_config('url','request_data_url')
    env = get_config('env','env_type')


    # Adding Base path to create Full path
    csv_save_path = full_path(csv_save_path)
    image_save_path = full_path(image_save_path)
    producte_url_csv = full_path(producte_url_csv)

    # load csv data of product_links
    data = get_data_url(request_data_url)

    # create of Embedding product image
    embeddings, df_embedding = create_embed(data, image_save_path, load_model(),request_image_url)

    # Call cosine_similarity function
    if embeddings is not None : 
        cosine_similarities = cosine_similarity(embeddings, embeddings)

    # Call create_cosine_similarity function
        cosine_similarity_df = create_cosine_similarity(df_embedding, cosine_similarities,csv_save_path,env)
        print("Cosine similarities calculated and saved.")
        upload(csv_save_path,env)
        print("File uploaded")

    else : 
        print("embeddings is None")

if __name__=="__main__":
    main()
