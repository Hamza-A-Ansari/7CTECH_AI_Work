from src.helpers.HttpClient import *
from src.training.csv import  *
from tqdm import tqdm
import pandas as pd 
import math
import re
import requests
import json
from collections import Counter


def check_tag(tag,tag_values):
    return int(tag) in tag_values


def transformation(data, feature_registry_csv, column, csv_save_path,api_data):
    """
    Perform transformation on data and save the result to a CSV file.

    Parameters:
    data (dict): Dictionary containing data to be transformed.
    feature_registry_csv (pandas.DataFrame): DataFrame containing feature registry data.
    column (str): Name of the column in feature_registry_csv containing tag cloud.
    csv_save_path (str): Path to save the resulting CSV file.

    Returns:
    pandas.DataFrame: DataFrame containing product IDs and tag strings, or None if an error occurs.
    """

    try:
        # Extract the tag id cloud from the feature registry
        tag_cloud = feature_registry_csv[column].tolist()

        # Convert values to integers, handling nan values
        tag_values = [int(x) if not math.isnan(x) else None for x in tag_cloud]

        product_ids = []  
        tag_strings = []

        if data["success"] == True:
            # Iterate over each dictionary in the "result" list
            for product_data in data["result"]:
                # Extract product ID
                product_id = product_data["productid"]

                # Extract tags for the current product
                tags = product_data[api_data]

                # Convert tags dictionary to a string
                tag_string = '  '.join([value for key, value in tags.items() if check_tag(key, tag_values)])

                # Append product ID and tag strings to lists
                product_ids.append(product_id)    
                tag_strings.append(tag_string)    

            # Create DataFrame for product tags
            product_tags_df = pd.DataFrame({'product_id': product_ids, 'tag_string': tag_strings})

            # Save DataFrame to CSV
            save_csv(product_tags_df,csv_save_path)

            # Log information
            print("Transformation completed. Result saved")
            logger.info(f"Transformation completed. Result saved to:{csv_save_path}")

            return product_tags_df
        else:
            # Log error if data retrieval was unsuccessful
            print("Error: Data retrieval unsuccessful.")
            logger.error("Error: Data retrieval unsuccessful.")
            return None
    except Exception as e:
        # Log and handle any exceptions
        print("An error occurred in function transformation :", str(e))
        logger.error("An error occurred in function transformation :", str(e))
        return None
 


def count_word_occurrences(input_string):
    """
    Count the occurrences of each word in the input string in a case-insensitive manner.
    
    Parameters:
    input_string (str): The input string to process.
    
    Returns:
    dict: A dictionary where the keys are unique words found in the input string (case-insensitive) 
          and the values are the number of occurrences of each word.
    
    """
    # Split the string into individual words
    words = re.findall(r'\b\w+\b', input_string.lower())
    # Count occurrences of each word
    word_counts = Counter(words)
    return word_counts 

def remove_substrings(original_string, substrings):
    """    
    Remove all occurrences of specified substrings from the original string.

    Parameters:
    original_string (str): The string from which substrings will be removed.
    substrings (list of str): A list of substrings to be removed from the original string.

    Returns:
    str: The modified string with all specified su"""
    for substring in substrings:
        
        original_string = original_string.replace(substring, '').replace('-','')
    return original_string.strip()


def transformation_tag_string(df=None, duplicate_substrng_tags=[], weighted_tag={}, csvpath=None):
    """
    Transform tag strings in a DataFrame and save the result to a CSV file.

    Parameters:
    df (pandas.DataFrame): DataFrame containing tag strings to be transformed.
    duplicate_substrng_tags (list of str): List of substrings to be removed from duplicate weighted tags.
    weighted_tag (dict): Dictionary containing weighted tag information.
    csvpath (str): Path to save the resulting CSV file.

    Returns:
    pandas.DataFrame: DataFrame containing transformed tag strings.
    """
    try :    
        
        tag_string_column = []
        collection_tag_clothing_df = df['tag_string'].tolist()
        for string in collection_tag_clothing_df:
            tags_in_product = [word for word, count in count_word_occurrences(string).items()]
            Not_weighted_tags = list(set(tags_in_product) - set(weighted_tag.get('result', [])))

            string_list = remove_substrings(string, ["clothing","Clothing",])
            string_list = string_list.split()
            
            if 'result' in weighted_tag and isinstance(weighted_tag['result'], list):
                for list_String in string_list:
                    if list_String in weighted_tag['result']:
                        added_tag_string = remove_substrings(list_String, duplicate_substrng_tags)
                        string = string + " " + added_tag_string
                
            tag_string = remove_substrings(string, ["clothing","Clothing","accessories","Accessories"])
            tag_string = re.sub(' +', ' ', tag_string)  # Removing extra spaces
            tag_string_column.append(tag_string)
        
        df['tag_string1'] = tag_string_column
        df = df.drop(columns=['tag_string']).rename(columns={'tag_string1': 'tag_string'})
        save_csv(df,csvpath)
        return df
    except Exception as e:
        # Log and handle any exceptions
        print("An error occurred in function transformation_tag_string :", str(e))
        logger.error("An error occurred in function transformation_tag_string :", str(e))
        return None