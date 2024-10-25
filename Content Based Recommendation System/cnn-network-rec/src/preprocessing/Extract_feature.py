from src.Lib.libraries import *
# Function to extract features from an image

def extract_features(img_path, model):
    """
    Extract features from an image using a pre-trained model.

    This function loads an image from the specified path, preprocesses it for the given model,
    extracts features, normalizes the features, and returns the resulting feature vector.

    Parameters:
    img_path (str): The path to the image file.
    model (keras.Model): A pre-trained model used to extract features from the image.

    Returns:
    numpy.ndarray: A normalized feature vector extracted from the image.
                   Returns None if the image file is not found.
                   
    """
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        expanded_img_array = np.expand_dims(img_array, axis=0)
        preprocessed_img = preprocess_input(expanded_img_array)
        result = model.predict(preprocessed_img).flatten()
        normalized_result = result / norm(result)
        return normalized_result
    except FileNotFoundError:
        print(f"File not found: {img_path}")
        return None


