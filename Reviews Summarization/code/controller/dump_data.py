from src.lib.Libraries import *
from src.handlers.api_handler import dump_data
from src.helper.Config import get_config
from src.helper.Logger import get_logger


logger = get_logger(__name__)


def dumping_db(json_data):

    log_key = "dumping_db"

    try:
        if json_data:

            data_dump_url = get_config('api', 'dump_url')

            response = dump_data(data_dump_url,json_data,log_key)

            logger.info(f'{log_key} Data dumped successfully: {response}')

    except Exception as e:
        logger.error(f"{log_key} Error occurred: {e}")

    

        