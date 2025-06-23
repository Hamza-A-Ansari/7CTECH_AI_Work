from src.lib.Libraries import *
from models.model import load_tokenizer
from src.handlers.api_handler import make_request
from src.handlers.Text_handler import tags_handler
from src.helper.Config import get_config
from src.helper.Logger import get_logger

logger = get_logger(__name__)

def data_model_loader():

    log_key = "data_model_loader "
    logger.info(f'......Satrting {log_key}......')

    # Load the reviews dataset and models
    try:
        # Load Tokenizer
        tokenizer_model = load_tokenizer(log_key)

        # Product ID API from Config
        product_ids_api = get_config('api', 'product_ids_api')

        # Fetch Product IDs
        fetch_product_ids = make_request(product_ids_api, log_key)

        # API for Review table in database
        summary_api = get_config('api', 'summary_table')

        # Extract Review table from database
        summary_data = make_request(summary_api, log_key)

        # Extract the "data" part
        summary_data = summary_data.get("data", [])

        # Convert to pandas DataFrame
        existing_data = pd.DataFrame(summary_data)

        # Tags API from Config
        tags_api = get_config('api', 'tags_api')

        # Fetch Tags API response
        tags_api_response = make_request(tags_api, log_key)

        # Extract tags that needs to be extracted
        product_tags = tags_handler(tags_api_response, log_key)

        # Exclude tags API from Config
        exclude_tags_api = get_config('api', 'tags_to_exclude_api')

        # Fetch Exclude Tags API response 
        exclude_tags_api_response = make_request(exclude_tags_api, log_key)

        # Extract tags that needs to be excluded
        tags_to_exclude = tags_handler(exclude_tags_api_response, log_key, exclude=True)

    except Exception as e:
        logger.error(f"{log_key} Error occurred: {e}")
        tokenizer_model = 0
        fetch_product_ids = 0
        existing_data = 0
        product_tags = 0
        tags_to_exclude = 0

    return tokenizer_model, fetch_product_ids, existing_data, product_tags, tags_to_exclude