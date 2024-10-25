from src.Lib.libraries import *
import pandas as pd


def load_csv(csv_path):

    df= pd.read_csv(csv_path)
    print(f"csv loaded from directory : {df}")
    logging.info("---- csv loaded -----    ")

    return df 

def save_csv(df, csv_save_path,env):
    try:
        os.makedirs(csv_save_path, exist_ok=True)
        csv_path = f"cosine_similarity_{env}_CNN.csv"
        csv_save_path = os.path.join(csv_save_path,csv_path)
        df.to_csv(csv_save_path, index=False)
        logging.info(f"Cosine_Similarity_file_Saved --- Path : {csv_save_path}")
        print(f"Cosine_Similarity_file_Saved --- Path : {csv_save_path}")
    except Exception as e:
        print(f"Error saving CSV file: {e}")
        logging.error(f"Error saving CSV file: {e}")
