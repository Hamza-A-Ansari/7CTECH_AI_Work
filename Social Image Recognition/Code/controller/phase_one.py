from src.helper.HttpClient import instagram_download
from src.preprocessing.prompt import cat_prompt
from src.prediction.prediction import prediction
from src.helper.Logger import get_logger
from src.helper.Config import config_file
from model.gemini import gemini_model
from src.lib.Liabraries import *

logger = get_logger(__name__)


def category_prediction(endpoint, log_key):

    log_key += "phase one "
    log_key += "func category prediction"
    logger.info(f"{log_key}")

    try:
        insta_image_path = instagram_download(endpoint, log_key)

        # Instagram image
        image_pil = Image.open(insta_image_path)

        # Extract the keys from the specified section
        config = config_file()
        api_keys = [value for _, value in config.items("gemini_api_key")]

        for api_key in api_keys:
            try:
                # Configure Gemini model
                model = gemini_model(api_key=api_key, log_key=log_key)

                # Category Prediction
                category_prompt = cat_prompt()
                response = prediction(model, request=[category_prompt , image_pil], log_key=log_key)
                response = json.loads(response)

                # If prediction is successful, break the loop
                break

            except Exception as e:
                logger.error(f"{log_key} api key {api_key} error {e}")
                
                # If this was the last API key, raise the exception
                if api_key == api_keys[-1]:
                    raise

                # Otherwise, continue to the next API key
                continue

        first_dict = response[0]

        if first_dict['ID'] == 0:
            return image_pil, 0, insta_image_path
        else:
            return image_pil, response, insta_image_path

    except Exception as e:
        logger.error(f"{log_key} error {e}")
        return 0, 0, insta_image_path
