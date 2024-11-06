from src.helper.Logger import get_logger
from src.lib.Liabraries import *


logger = get_logger(__name__)


def vactor_tranformation(vector1, vector2):

    # Reshape vectors to have compatible shapes for cosine similarity calculation
    vector1 = np.array(vector1).reshape(1, -1)
    vector2 = np.array(vector2).reshape(1, -1)

    return vector1, vector2


def dataframe(data, columns):

    df = pd.DataFrame(data, columns=columns)

    return df


def response_to_df(response):

    data = [x.split(",") for x in response.split("\n") if x.strip()]
    df = dataframe(data[1:], data[0])

    return df


# Function to convert list to space-separated string with hyphens
def convert_list_to_string(lst):
    if isinstance(lst, list):
        return " ".join([item.replace(" ", "-") for item in lst if item != "null"])
    return lst


def res_trans(tags_data, cat_data, log_key):

    log_key += " func res trans"

    logger.info(f"{log_key}")

    try:

        # Normalize the list of dictionaries
        df = pd.json_normalize(tags_data)
        cat_df = pd.json_normalize(cat_data)

        # Apply the function to each column
        for column in df.columns:
            df[column] = df[column].apply(convert_list_to_string)

        new_df = pd.DataFrame()
        new_df["ID"] = df["ID"]
        new_df["tag_string"] = df.iloc[:, 1:].apply(
            lambda row: " ".join(row.dropna()), axis=1
        )

        new_df['tag_string'] = new_df['tag_string'].str.lower()

        new_df['tag_string'] = new_df['tag_string'].replace('and ', ' ', regex=True)
        new_df['tag_string'] = new_df['tag_string'].replace('null', ' ', regex=True)
        new_df['tag_string'] = new_df['tag_string'].replace('none', ' ', regex=True)
        new_df['tag_string'] = new_df['tag_string'].str.replace(',+', ' ', regex=True).str.strip()
        new_df['tag_string'] = new_df['tag_string'].str.replace(r'[\"\[\]]', '', regex=True)
        new_df['tag_string'] = new_df['tag_string'].str.replace(r'\s+', ' ', regex=True)

        cat_df["ID"] = cat_df["ID"].astype(int)
        new_df["ID"] = new_df["ID"].astype(int)

        merged_df = pd.merge(cat_df, new_df, on="ID", how="inner")

        return merged_df

    except Exception as e:
        logger.error(f"{log_key} error {e}")
        return pd.DataFrame()
