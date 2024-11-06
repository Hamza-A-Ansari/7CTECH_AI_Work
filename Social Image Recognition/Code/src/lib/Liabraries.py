import pandas as pd
import numpy as np
import re 
from tqdm import tqdm
import concurrent.futures
from io import StringIO

import configparser
import glob

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import google.generativeai as genai

from PIL import Image

import requests
import os
import json
import logging

