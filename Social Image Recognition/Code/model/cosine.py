from src.preprocessing.preprocessing import *
from src.transformation.transformation import vactor_tranformation
from src.lib.Liabraries import *
from src.helper.Logger import get_logger

logger = get_logger(__name__)

def cosine_model(df,log_key):
    
    log_key += " func cosine model"

    try : 
        product_tag_id = [id for id in df['product_id']][1:]
        
        df_pd = df
        df_pd['tag_string'] = df_pd['tag_string'].fillna('').apply(custom_preprocessor)
        preprocessed_text = df_pd['tag_string'].apply(preprocess_text)
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(preprocessed_text)
        tfidf_tokens = vectorizer.get_feature_names_out()
        tfidf_vector = X.toarray().tolist()

        tfidf_vector_1 = tfidf_vector[0]

        cosine_scores = []
        for i in range(1, len(tfidf_vector)):
            vector1, vector2 = vactor_tranformation(tfidf_vector_1, tfidf_vector[i])

            # Calculate cosine similarity
            similarity = cosine_similarity(vector1, vector2)
            similarity = similarity[0][0]
            cosine_scores.append(similarity)

        cosin_df = pd.DataFrame({'product_id':product_tag_id, 'Cosine_Score': cosine_scores})
        cosin_df = cosin_df.sort_values(by='Cosine_Score', ascending = False)


        logger.info(f'{log_key} computed cosine')

        return cosin_df

    except Exception as e:
        logger.error(f"{log_key} error {e}")
        return None