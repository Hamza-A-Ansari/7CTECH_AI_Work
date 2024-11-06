from src.helper.Config import config_file
from src.helper.Logger import get_logger
from src.preprocessing.prompt import tags_prompt
from src.prediction.prediction import prediction
from src.transformation.transformation import res_trans
from model.gemini import gemini_model
from src.lib.Liabraries import *

# logKey = f"category_prediction ednppiont {endpoint} id {id}"

logger = get_logger(__name__)


def tags_prediction(image_pil, response, log_key):

    log_key += "phase two "
    log_key += "func tags prediction"
    logger.info(f"{log_key}")

    try:
        config = config_file()
        api_keys = [value for _, value in config.items("gemini_api_key")]

        for api_key in api_keys:
            try:
                # Configure Gemini model
                model = gemini_model(api_key=api_key, log_key=log_key)

                # tag response
                tag_prompt = tags_prompt(response)
                tags_response = prediction(model, request=[tag_prompt, image_pil], log_key=log_key)
                tags_response = json.loads(tags_response)
                cat_df = res_trans(tags_response, response, log_key)

                # If prediction is successful, break the loop
                break

            except Exception as e:
                logger.error(f"{log_key} api key {api_key} error {e}")

                # If this was the last API key, raise the exception
                if api_key == api_keys[-1]:
                    raise

                # Otherwise, continue to the next API key
                continue

        return cat_df

    except Exception as e:
        logger.error(f"{log_key} error {e}")
        return pd.DataFrame()
