import pandas as pd



def load_csv(csv_path):
    '''
    Load a CSV file into a Pandas DataFrame.
    
    Parameters:
    csv_path (str): The file path to the CSV file.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the data from the CSV file.
    '''
    df = pd.read_csv(csv_path)
    
    return df


def save_csv(df,save_csv_path):
    """ 
    Save a Pandas DataFrame to a CSV file.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame to save to a CSV file.
    save_csv_path (str): The file path where the CSV file will be saved.
    
    Returns:
    pandas.DataFrame: The same DataFrame that was passed in as an argument."""
    

    df.to_csv(save_csv_path,index = False)

    return df