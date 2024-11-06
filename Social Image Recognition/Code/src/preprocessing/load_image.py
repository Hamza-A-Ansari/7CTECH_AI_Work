from src.helper.Logger import get_logger
from src.lib.Liabraries import *

logger = get_logger(__name__)

def generate_paths(base_path, ids):
    """
    The function `generate_paths` creates a list of file paths by joining a base path with a list of IDs
    and appending a file extension.
    
    :param base_path: The `base_path` parameter is a string representing the base directory path where
    the image files are located or where you want to generate paths to
    :param ids: The `ids` parameter in the `generate_paths` function is a list of identifiers that will
    be used to generate file paths
    :return: The function `generate_paths` returns a list of file paths by joining each `id` from the
    `ids` list with the `base_path` and appending the ".jpg" extension to it.
    """
    paths = [os.path.join(base_path, f"{id}.jpg") for id in ids]
    return paths


def check_files_exist(paths,log_key):
    """
    The function `check_files_exist` checks if files exist in the specified paths and returns a list of
    existing files.
    
    :param paths: The `check_files_exist` function takes a list of file paths as input and checks if
    each file exists in the system. It then returns a list of paths that actually exist in the system
    :return: The function `check_files_exist` returns a list of paths that exist in the given list of
    paths. It filters out the paths that do not exist and prints an error message for each non-existing
    path.
    """
    log_key += "func check file exist"

    existing_files = [path for path in paths if os.path.exists(path)]
    for path in paths:
        if not os.path.exists(path):
            logger.info(f"{log_key} no image {path}")

    return existing_files



def load_images(image_paths,review_image,log_key):
    """
    The function `load_images` loads images from specified paths, converting them to RGB mode if
    necessary, and returns a list of loaded images.
    
    :param image_paths: The `image_paths` parameter in the `load_images` function is a list of file
    paths to the images that you want to load. The function iterates over each path in the list,
    attempts to open the image file using `Image.open(path)`, and then appends the loaded image to
    :return: The function `load_images` is returning a list of image paths and corresponding image
    objects that have been successfully loaded from the provided `image_paths`.
    """
    log_key += " func load images"
    images = []

    for path in image_paths:
        try:
            img = Image.open(path)
            if img.mode == 'P':
                img = img.convert('RGB')

            directory, file_name = os.path.split(path)

            # Further split the file name into name and extension
            file_name_without_extension, file_extension = os.path.splitext(file_name)
            images.append(f"Product ID: {file_name_without_extension}")
            images.append(img)


        except Exception as e:
            logging.error(f"{log_key} error loading image {path} {e}")

    images.append("This is a review image ")
    images.append(review_image)
    return images