from src.lib.Liabraries import *
from src.helper.Logger import get_logger

logger = get_logger(__name__)

def delete_image(image_path, log_key):

    log_key += "func delete image"
    logger.info(f"{log_key}")
    
    if image_path != 0:
        if os.path.exists(image_path):

            try:
                os.remove(image_path)
                logger.info(f"{log_key} insta image deleted")

            except Exception as e:
                logger.error(f"{log_key} error {e}")
        else:
            logger.info(f"{log_key} image does not exist")

    logger.info(f"{log_key} Process Completed")

    