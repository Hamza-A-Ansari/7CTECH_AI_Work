from src.helpers.HttpClient import *
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd
from nltk.tokenize import word_tokenize
import pandas as pd
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re 



nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

custom_stopwords = set(stopwords.words('english'))


def custom_preprocessor(text):
    """
    The custom_preprocessor function converts text to lowercase if it is a string, otherwise it returns
    an empty string.
    
    :param text: The `text` parameter is the input data that will be processed by the
    `custom_preprocessor` function. The function checks if the input `text` is a string, and if it is,
    it converts the text to lowercase. If the input is not a string, it handles it by converting
    :return: An empty string is being returned if the input `text` is not a string.
    """
    # Check if text is a string
    if isinstance(text, str):
        return text.lower()  # Convert to lowercase if it's a string
    else:
        # Handle non-string data appropriately (e.g., convert to an empty string)
        return ''
def preprocess_text(text):
    """
    The `preprocess_text` function takes a text input, splits hyphenated words, removes plural forms and
    's', lemmatizes words, removes stop words, and returns the preprocessed text.
    
    :param text: The `preprocess_text` function takes a text input and performs several preprocessing
    steps on it. These steps include splitting hyphenated words, removing plural forms and 's',
    lemmatizing words, removing stop words, and joining the filtered tokens back into a string
    :return: The function `preprocess_text` returns a preprocessed version of the input text. This
    includes splitting hyphenated words, removing plural forms and 's', lemmatizing words, removing stop
    words, and joining the filtered tokens into a single string.
    """

    # Split hyphenated words
    text = re.sub(r'[-]', ' ', text)
    tokens = word_tokenize(text)
    filtered_tokens = []
    for word in tokens:
        # Remove plural forms and 's'
        word = re.sub(r's$', '', word)
        # Lemmatize and remove stop words
        word = lemmatizer.lemmatize(word)
        if word.lower() not in custom_stopwords and len(word) > 1:
            filtered_tokens.append(word)
    return ' '.join(filtered_tokens)

def model_train(df=None):
    '''

    Train a model using TF-IDF vectorization and calculate cosine similarity between product tags.
    
    Parameters:
    df (pandas.DataFrame): A DataFrame containing at least 'product_id' and 'tag_string' columns.
    
    Returns:
    pandas.DataFrame: A DataFrame containing product pairs and their cosine similarity scores, 
                    or None if an error occurs.
    
    '''
    try :
        print("Model Training Started")
        product_tag_id = [id for id in df['product_id']]
        


        df_pd = df

        df_pd['tag_string'] = df_pd['tag_string'].fillna('').apply(custom_preprocessor)
        preprocessed_text = df_pd['tag_string'].apply(preprocess_text)
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(preprocessed_text)
        tfidf_tokens = vectorizer.get_feature_names_out()
        tfidf_vector = X.toarray().tolist()
        # print(tfidf_tokens)
        # print(X)
        
        # print(tfidf_vector)

        cos_sim = cosine_similarity(X,X)

        all_product_combination = {'Product_A': [], 'Product_B': [],'cosin_score': []}
        
        for i in range(len(cos_sim)):
            for j in range(1, len(cos_sim)):
                all_product_combination['Product_A'].append(product_tag_id[i])
                all_product_combination['Product_B'].append(product_tag_id[j])
                all_product_combination['cosin_score'].append(float(cos_sim[i][j]))

        df= pd.DataFrame(all_product_combination)

        
        return  df
    except Exception as e:
        # Log and handle any exceptions
        print("An error occurred in function model :", str(e))
        logger.error("An error occurred in function model :", str(e))
        return None