from src.Lib.libraries import *

def Download_images(image_path, image_save_folder, url_response):
    """
    Save an image from a URL response to a specified folder.

    This function creates the necessary directories, saves the image data from the URL response
    to the specified folder, and logs the process.

    Parameters:
    image_path (str): The path or name of the image file to be saved.
    image_save_folder (str): The folder path where the image will be saved.
    url_response (bytes): The binary content of the image obtained from the URL response.
    """
    try:
        os.makedirs(image_save_folder, exist_ok=True)
        filename = os.path.splitext(image_path)[0]
        image_save_full_path = os.path.join(image_save_folder, f"{image_path}")
        with open(image_save_full_path, 'wb') as file:
            file.write(url_response)
        print(f"Image saved for product: {image_path}")
        logging.info(f"Image saved for product: {image_path}")
    except Exception as e:
        print(f"Error saving image for product {image_path}: {e}")
        logging.error(f"Error saving image for product {image_path}: {e}")