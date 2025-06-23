from src.lib.Libraries import *
from src.helper.Logger import get_logger
from src.helper.Config import get_config

logger = get_logger(__name__)

def tags_handler(tags_api_response, log_key, exclude=False):

    if exclude == False:

        log_key += 'tags_handler (product tags)'

        try:    
            # Load your CSV file
            csv_path = f"{get_config('directories', 'csv_dir')}/{get_config('csv', 'csv_path')}"
            df = pd.read_csv(csv_path)

            # Get valid tag/category IDs from the CSV
            valid_ids = set(df['tag_cloud'].astype(str))

            # Final dictionary
            product_dict = {}

            # Process each product
            for product in tags_api_response['result']:
                pid = product['productid']
                tags = product.get('tags', {})
                categories = product.get('categories', {})
                
                # Filter using valid_ids
                filtered_tags = [v for k, v in tags.items() if k in valid_ids]
                filtered_categories = [v for k, v in categories.items() if k in valid_ids]
                
                # Combine and create comma-separated string
                combined = ', '.join(filtered_tags + filtered_categories)
                
                # Add to dictionary
                product_dict[pid] = combined

            return product_dict
        
        except Exception as e:
            logger.error(f"{log_key} Error occurred: {e}")
            return {}
        
    else:
        log_key += 'tags_handler (tags excluded api)'
        try:
            keywords = [item["keyword"] for item in tags_api_response]

            return keywords

        except Exception as e:
            logger.error(f"{log_key} Error occurred: {e}")
            return []


class ResponseFormat(BaseModel):
    summary: str
    keywords: List[str]


def clean_text(text, log_key):

    log_key += 'clean_text '

    try:
        # Decode URL-encoded characters (e.g., %2c)
        decoded_text = unquote(text)

        # Replace specific unwanted symbols but keep punctuation
        cleaned_text = re.sub(r'[^a-zA-Z0-9\'.,!?;: ]+', ' ', decoded_text) #re.sub(r'[^a-zA-Z0-9 ]+', ' ', decoded_text)

        # Remove any extra whitespace
        return ' '.join(cleaned_text.split())
    except Exception as e:
        logger.error(f"{log_key} Error occured: {e}")
        return None
    

def format_summary(input_text, log_key):

    log_key += 'format_customer_say '
    
    try:
        # Remove semicolon
        input_text = input_text.replace(';', ',')

        # Remove quotes
        input_text = input_text.replace('"', '')

        # Capitalize the first letter and after full stops
        sentences = input_text.split('. ')
        formatted_sentences = [sentence.capitalize() for sentence in sentences]
        formatted_text = '. '.join(formatted_sentences)

        # Ensure the text ends with a full stop
        if not formatted_text.endswith('.'):
            formatted_text += '.'

        return formatted_text
    except Exception as e:
        logger.error(f"{log_key} Error occured: {e}")
        return None
    

def format_keywords(keywords, log_key):

    log_key += 'format_keywords '

    try:
        # Split the keywords by commas, strip spaces, capitalize each, and join back
        capitalized_keywords = ', '.join(word.strip().replace('"', '').capitalize() for word in keywords)
        return capitalized_keywords
    
    except Exception as e:
        logger.error(f"{log_key} Error occured: {e}")
        return None


# Function to extract "Custom" and "Keyword" from the response
def extract_summary_and_keywords(response, product_tags, tags_to_exclude, log_key):

    log_key += 'extract_custom_and_keywords '

    try:
        # Extract summary and keywords from response
        summary = response["summary"]
        keywords = response["keywords"]

        if product_tags != 0:
            product_tags = [tag.strip() for tag in product_tags.split(',')]

            keywords = (lambda b_set: [item for item in keywords if item.lower() not in b_set])(set(map(str.lower, product_tags)))

        keywords = (lambda b_set: [item for item in keywords if item.lower() not in b_set])(set(map(str.lower, tags_to_exclude)))

        # Convert to one line if the text contains multiple lines
        if "\n" in summary:
            summary = " ".join(line.strip() for line in summary.splitlines() if line.strip())

        # Format Summary
        if summary:
            formatted_summary = format_summary(summary, log_key)
        else:
            formatted_summary = ''

        # Format Keywords
        if keywords:
            formatted_keywords = format_keywords(keywords, log_key)
        else:
            formatted_keywords = ''

        return formatted_summary, formatted_keywords 
    
    except Exception as e:
        logger.error(f"{log_key} Error occured: {e}")
        return None
