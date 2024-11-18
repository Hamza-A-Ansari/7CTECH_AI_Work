import logging
from PIL import Image
import pandas as pd
import time 
import requests
import os
import configparser
import glob
import google.generativeai as genai
import csv
import json
from io import StringIO
# Configure logging
os.makedirs('logs', exist_ok=True)

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create file handler to write logs to a file
file_handler = logging.FileHandler('logs/app.log')
file_handler.setLevel(logging.INFO)

# Create stream handler to print logs to the terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# Define the log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)