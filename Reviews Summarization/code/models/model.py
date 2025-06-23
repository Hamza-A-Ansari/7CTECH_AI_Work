from src.lib.Libraries import *
from src.helper.Config import get_config
from src.helper.Logger import get_logger
from src.handlers.Text_handler import ResponseFormat

logger = get_logger(__name__)


def load_tokenizer(log_key):

    log_key += 'load_tokenizer '

    try:
        model_name = get_config('model', 'tokenizer')
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        return tokenizer
    except Exception as e:
        logger.error(f"{log_key} Error loading tokenizer for model {model_name}: {e}")
        return None


def request_model(instructions, product_tags, categ, reviews, log_key):

    log_key += 'request_model '
    url = get_config('api', 'model_api')

    try:
        # Prompt and instructions
        prompt = f"Summarize the reviews according to the given instructions. Note that you should not include any information about occasions, events, or reasons for purchasing strictly and full focus should be on product fit only in summary: \n\n{categ}\n\n{reviews}"
        if product_tags != 0:
            product_tags = f'\nDo not pick below keywords from the reviews: \n{product_tags}'
            instructions += product_tags

        # Creating client model
        client = OpenAI(base_url=url,api_key="ollama")

        # Requesting model
        response = client.beta.chat.completions.parse(
            model = get_config('model', 'summarization_model'),

        messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": prompt}
            ],
        response_format = ResponseFormat, 
        temperature = float(get_config('model', 'temperature'))
        )
        
        return json.loads(response.choices[0].message.content)
    
    except Exception as e:
        logger.error(f"{log_key} Error occured: {e}")
        return None
