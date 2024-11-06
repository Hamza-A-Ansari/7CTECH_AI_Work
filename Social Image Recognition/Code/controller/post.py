from src.lib.Liabraries import *
from src.helper.Config import get_config
from src.helper.Logger import get_logger

logger = get_logger(__name__)

def post_results(id, result, log_key):

    log_key += "func post results"
    logger.info(f"{log_key}")

    result = [x for x in result if x != 0 and x != '0']

    if not result:
        logger.info(f"{log_key} nothing to upload")
        
    else:
        logger.info(f'{log_key} uploading results {result}')

        try:
            id = int(id)
            input_data = {
                "id": id,
                "product_ids": result,
                "status": 4
            }

            url = get_config('api', 'result_api')
            token = get_config('tokens', 'post_token')

            header = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }

            response = requests.post(url, json=input_data, headers=header)

        except Exception as e:
            logger.error(f"{log_key} error {e}")