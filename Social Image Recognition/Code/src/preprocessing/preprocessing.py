from src.lib.Liabraries import *

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')

def custom_preprocessor(text):
    # Check if text is a string
    if isinstance(text, str):
        return text.lower()  # Convert to lowercase if it's a string
    else:
        # Handle non-string data appropriately (e.g., convert to an empty string)
        return ''

def preprocess_text(text):


    lemmatizer = WordNetLemmatizer()
    custom_stopwords = set(stopwords.words('english'))

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

