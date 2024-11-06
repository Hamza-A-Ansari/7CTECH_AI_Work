from src.lib.Liabraries import *
from src.helper.Logger import get_logger

logger = get_logger(__name__)

def prediction(model, request, log_key):

    log_key += " func prediction"

    try:
        response = model.generate_content(request,
                                    request_options={"timeout": 600}
                                    )
        response.resolve()
        return response.text
    except Exception as e:
        logger.error(f"{log_key} error {e}")
