from src.lib.Libraries import *
from src.helper.Logger import get_logger

logger = get_logger(__name__)

def token_counter(text,tokenizer_model, log_key):

    log_key += 'token_counter '

    try:
        # Tokenize the entire text
        tokens = tokenizer_model.encode(text, truncation=False)
    
        return tokens
    except Exception as e:
        logger.error(f"{log_key} Error occured: {e}")
        return None