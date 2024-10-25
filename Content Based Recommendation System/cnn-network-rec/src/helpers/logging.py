from src.Lib.libraries import *



def create_log_file():
    logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')