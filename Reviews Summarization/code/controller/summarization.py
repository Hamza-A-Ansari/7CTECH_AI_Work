from src.lib.Libraries import *
from models.model import request_model
from src.handlers.Text_handler import extract_summary_and_keywords, clean_text
from src.handlers.Token_handler import token_counter
from src.handlers.api_handler import fetch_reviews
from src.helper.Config import get_config
from src.helper.Logger import get_logger
from src.handlers.prompt import instructions


logger = get_logger(__name__)

def summarizer(tokenizer_model, fetch_product_ids, existing_data, product_tags, tags_to_exclude):

    updated_results = []
    for product in fetch_product_ids:

        log_key = f"Pid: {product.get('product_id')} - summarizer "

        try:
            # Ensure product is a dictionary
            if not isinstance(product, dict):
                logger.info(f"{log_key} Skipping invalid product data: {product}")
                continue
            
            # Extract product ID and category
            product_id = product.get("product_id")
            product_categ = product.get("product_category")

            # If productId does not exit continue
            if not product_id:
                continue

            # Review URL from Config
            review_url = get_config('api', 'review_url')

            # Fetching reviews from API
            reviews = fetch_reviews(product_id, review_url, log_key)

            # If no reviews, skip this product
            if not reviews:
                continue

            # Extract valid reviews
            valid_reviews = [review for review in reviews if review.get("text")]

            # If no valid reviews, skip this product
            if not valid_reviews:
                continue
                
            # Join all reviews into a single string
            all_reviews = "\n".join(
                [
                    f"Review: {review.get('text', 'No Text')}"
                    for review in reviews
                ]
            )
            
            # Defining category of the product
            categ = f'Category of this product is: {product_categ}'

            # Clean text
            input_text = clean_text(all_reviews, log_key)

            # Count tokens from reviews 
            tokens = token_counter(input_text, tokenizer_model, log_key)

            inp_token = len(tokens)

            # Skip product if review tokens are less than or equal to 100
            if inp_token < 50:
                continue

            # Check if the product ID already exists in the data
            existing_row_index = existing_data[existing_data["product_id"] == product_id].index

            if not existing_row_index.empty:
                # Extract the previous token count
                previous_token = existing_data.loc[existing_row_index, 'token'].values[0]

                # Calculate the percentage difference between the previous and current token counts
                token_diff_percentage = abs(inp_token - previous_token) / previous_token
                
                # Compare the previous token with the current token
                token_difference = float(get_config('range', 'token_difference'))
                if token_diff_percentage < token_difference:
                    continue
            
            # Extract tags from current product
            current_product_tags = product_tags.get(int(product_id), 0)
            
            # Call model for generating summaries
            response = request_model(instructions, current_product_tags, categ, reviews, log_key)

            # Extracting summary and keywords from response
            customers_say_text, keywords_text = extract_summary_and_keywords(
                response, current_product_tags, tags_to_exclude, log_key)

            # Skip this iteration if either is empty
            if not customers_say_text or not keywords_text:
                continue  
            
            # Create a new row with results
            new_row = {
            "product_id": product_id,
            "token": inp_token,
            "summary": customers_say_text,
            "keyword": keywords_text,
            }
  
            logger.info(f"{log_key} Generated Response: {new_row}")
            updated_results.append(new_row)

        except Exception as e:
            logger.error(f"{log_key} Error occurred: {e}")
            updated_results = 0

    return updated_results

    
