from src.training.TransfromationData import * 
from src.helpers.HttpClient import *
from src.training.csv import *
from models.model import *
import pandas as pd
import os 


logger = get_logger(__name__)

def train():

    # Base Url for Request to fetch All data 
    base_url = get_config('url', 'main_api')
    endpoint = get_config('url', 'endpoint')

    BASE_PATH=os.getcwd()
    feature_list_path = os.path.join(BASE_PATH, 'data', 'feature_registry').replace('\\', '/')
    cosin_path=os.path.join(BASE_PATH,'cosin_similarity_csv').replace('\\', '/')
    transformation_csv_path=f"{BASE_PATH}/{get_config('data_transformation','path')}"


    try:
        os.makedirs(transformation_csv_path,exist_ok=True)
        print(transformation_csv_path)
    except:
            logger.info(f"FOLDER ALREADY EXIST{transformation_csv_path}")

    try:
        os.makedirs(feature_list_path,exist_ok=True)
        print(feature_list_path)
    except:
            logger.info(f"FOLDER ALREADY EXIST{feature_list_path}")



    try:
        os.makedirs(cosin_path,exist_ok=True)
        print(cosin_path)
    except:
            logger.info(f"FOLDER ALREADY EXIST{cosin_path}")







    Features_clothing_df = f"{feature_list_path}/{get_config('feature_list', 'feature_list_clothing')}"
    Features_accesories_df=f"{feature_list_path}/{get_config('feature_list','feature_list_accessories')}"


    data = fetch_api_status(base_url,endpoint)



    url='https://dev-api.fashionpass.com/api/v1/Collections/GetCategoryTreeTags?level=2'
    duplicate_substrng_tags = ['sleeve', 'shoulder', 'dresses', 'bags', 'necklaces', 'earrings', 'neck', 'belts', 'denim', 'sunglasses']
    # duplicate_substrng_tags = ['sleeve', 'shoulder']
    weighted_tag= {"success":True,"result":["clothing","accessories","activewearandloungewear",r"*dresses","jacketscoatsandblazers","jeansanddenim","jumpsuits","Jumpsuits","maternity","pants","rompers","shorts","skirts","sweatersandknits","tops","swimwear","twopieceset","postpartum","basics","belts","bags","hatsandhairaccessories","jewelry","scarvesandbeanies","sunglassesandeyewear","fpmerch","shoes","intimates","mini","midi","maxi","sundresses","slipdresses","wrapdresses"]}

    feature_registry = load_csv(Features_clothing_df)



    # ------------------------------------------------------------------------------------------------------------
    # Tag_collection csv path and function

    logger.info (f'transformation tag_cloud started')

    column1 = get_config('feature_list_columns','column1')
    
    api_key = "tags"



    t1_clothing_df=f"{transformation_csv_path}/{get_config('data_transformation','t1_clothing_df')}"


    csv_cosin_path1=f"{cosin_path}/{get_config('cosin_similarity_path','cs1')}"


    save_csv(model_train(transformation_tag_string(transformation(data,feature_registry,column1,t1_clothing_df,api_key),duplicate_substrng_tags,weighted_tag,t1_clothing_df)),csv_cosin_path1)

    logger.info (f'transformation tag_cloud ended')
