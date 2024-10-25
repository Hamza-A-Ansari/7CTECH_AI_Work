from src.helpers.Config import get_config
from src.helpers.Logger import get_logger
from src.training.csv import *
import pandas as pd
from datetime import date
import os

logger = get_logger(__name__)

def val():
    """
    The function `val` reads data from a cosine similarity CSV file, processes it to generate product
    recommendations, and saves the results to a new CSV file.

    The function performs the following steps:
    1. Reads a cosine similarity CSV file.
    2. Filters and sorts the data based on a cosine score threshold.
    3. Generates recommendations for each unique product.
    4. Saves the processed recommendations to a new CSV file.

    Returns:
    None: The function returns `None` if an error occurs during its execution.
    """
    try  :
        logger.info('cosin csv started reading')

        BASE_PATH=os.getcwd()

        cosin_path=os.path.join(BASE_PATH,'cosin_similarity_csv').replace('\\', '/')
 
        cs1=f"{cosin_path}/{get_config('cosin_similarity_path','cs1')}"

        env = get_config('env', 'env')

        cs1 =load_csv(cs1)

        logger.info('cosin csv ended reading')
        cosin_df=[]


        th1=.30



        product_ids = cs1.Product_A.unique()



        print("total number of product",len(product_ids))

        for r in product_ids:
            print(r)
            cs1_product_b=[]

            try:
                cs1_product_b_so= cs1[(cs1['Product_A'] == r) & (cs1['cosin_score'] >= th1)]
                cs1_product_b = cs1_product_b_so.sort_values(by='cosin_score', ascending=False)
                cs1_product_b.to_csv("data.csv")
                cs1_product_b=cs1_product_b['Product_B'].unique().tolist()
                cs1_product_b=cs1_product_b[:35]            

            except:
                print('product does not exit in csv')



            my_dict = {i:cs1_product_b.count(i) for i in cs1_product_b}

            top_recomendation=[]
            for key,value in my_dict.items():
                top_recomendation.append(key)
            print('top re',top_recomendation)
            cosin_df.append(cs1[(cs1['Product_A']==r) & (cs1['Product_B'].isin(top_recomendation))])

        df=cosin_df[0]

        for i in cosin_df[1:]:
            try:
                df=df._append(i,ignore_index = True) 
            except:
                print('out of index')


        cosin_save_path = f"{cosin_path}/cosine_similarity_{env}_TFIDF.csv"

        save_csv(df,cosin_save_path)

        print('valdation csv part done')
        logger.info('valdation csv part done')


    except Exception as e:
        print("An error occurred in function val :", str(e))
        logger.error("An error occurred in function val :", str(e))
        return None