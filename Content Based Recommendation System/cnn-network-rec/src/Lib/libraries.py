import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
import numpy as np
from numpy.linalg import norm
import os
from tqdm import tqdm
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import requests
import pandas as pd
from configparser import ConfigParser 
import os
import urllib.request
import csv
import time
import logging
import glob