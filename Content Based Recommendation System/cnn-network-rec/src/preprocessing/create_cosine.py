from src.Lib.libraries import *
from src.preprocessing.csv import *


def create_cosine_similarity(df, cosine_similarities,csv_save_path,env):
    """
    Create a cosine similarity DataFrame and save it to a CSV file.

    This function generates a cosine similarity matrix from the provided DataFrame and NumPy array.
    It iterates over the matrix to save the similarity scores between product pairs, and then saves
    the results to a CSV file.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing product information, must include a 'product_id' column.
    cosine_similarities (numpy.ndarray): A NumPy array containing the cosine similarity scores.
    csv_save_path (str): The path where the resulting CSV file should be saved.
    env (str): The environment identifier to dev or live
    Returns:
    pandas.DataFrame: A DataFrame containing the cosine similarity scores between products.
    None: If an error occurs during the process."""
    try:
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input 'df' must be a DataFrame.")

        if not isinstance(cosine_similarities, np.ndarray):
            raise ValueError("Input 'cosine_similarities' must be a NumPy array.")

        product_ids = df['product_id'].tolist()
        num_products = len(product_ids)

        # Check if cosine similarities array has the correct shape
        if cosine_similarities.shape != (num_products, num_products):
            raise ValueError("Shape of cosine_similarities array does not match the number of products.")

        # Create a list to store the cosine similarity results
        similarity_results = []

        # Iterate over the cosine similarity matrix and save the results
        for i in range(num_products):
            for j in range(0 , num_products):
                similarity_results.append({
                    'original_product_id': product_ids[i],
                    'match_product_id': product_ids[j],
                    'cosine_similarity_score': cosine_similarities[i, j]
                })

        # Create a DataFrame from the list
        cosine_similarity_df = pd.DataFrame(similarity_results)
        save_csv(cosine_similarity_df,csv_save_path,env)
        # cosine_similarity_df.to_csv("cosin_similarity_result/cosine_similarity.csv")

        print("---- Cosine similarity CSV file created ----")

        logging.info("---- Cosine similarity CSV file created ----")

        return cosine_similarity_df

    except Exception as e:
        print(f"Error occurred: {e}")
        logging.exception("Error occurred", exc_info=True)
        return None