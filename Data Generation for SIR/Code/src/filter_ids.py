from helper.libraries import *

def filter_ids_not_in_csv(df, all_ids):
    try:

        # Load the CSV file
        product_ids_in_csv = df['product_id'].tolist()

        # Filter IDs that are not in the CSV
        filtered_ids = [id_ for id_ in all_ids if id_ not in product_ids_in_csv]
        logging.info(f"Filtered out {len(filtered_ids)} IDs that tag string are not in the tag collection csv.")

        return filtered_ids

    except Exception as e:
        logging.error(f"An error occurred while filtering IDs: {e}")
        return []