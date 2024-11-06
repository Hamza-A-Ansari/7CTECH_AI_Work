from src.lib.Liabraries import *
from src.helper.Config import get_config
from src.helper.Logger import get_logger
from src.helper.Config import get_config

logger = get_logger(__name__)

def gemini_model(api_key=None,system_information=None, log_key=None):

  log_key += " func gemeni model"

  try:

    genai.configure(api_key=api_key)

    # Set the model to Gemini 1.5 Pro.
    generation_config = {
      "max_output_tokens": 15000,
      "temperature": 0.0,
      "response_mime_type": "application/json",
    }
    safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_NONE"
    },
    ]

    # if system_information is not None:
    #       system_instruction = system_information
    # else: 
    #    system_instruction = None

    # Set up the model
    model = genai.GenerativeModel(model_name=get_config('model', 'gemini_model'),
                                      generation_config=generation_config, safety_settings=safety_settings,
                                      system_instruction=system_information
                                      )
    
    return model
  
  except Exception as e:
    logger.error(f"{log_key} error {e}")

    return None
