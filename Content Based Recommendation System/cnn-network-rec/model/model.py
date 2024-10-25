from src.Lib.libraries import *

def load_model():
    model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    model.trainable = False

    # Modify the model to include GlobalMaxPooling2D
    model = tensorflow.keras.Sequential([
        model,
        GlobalMaxPooling2D()
    ])
    logging.info("---- Resnet50 model Loaded ----")
    print("---- Resnet50 model Loaded ----")
    return model


def load_model():


    """
    Load and modify the ResNet50 model pretrained on ImageNet.
    
    The function performs the following steps:
    1. Loads the ResNet50 model with ImageNet weights, excluding the top layers.
    2. Sets the model layers to non-trainable.
    3. Adds a GlobalMaxPooling2D layer to the model.
    4. Logs and prints a message indicating the model has been loaded.

    Returns:
    tensorflow.keras.Model: The modified ResNet50 model."""
        
    model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    model.trainable = False

    # Modify the model to include GlobalMaxPooling2D
    model = tensorflow.keras.Sequential([
        model,
        GlobalMaxPooling2D()
    ])
    logging.info("---- Resnet50 model Loaded ----")
    print("---- Resnet50 model Loaded ----")
    return model