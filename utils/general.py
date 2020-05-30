import os
import sys
sys.path.append(os.getenv('BASEPATH'))

import logging
import json
from utils import constants as cst

from utils.encryptor import Encryptor

encryptor = Encryptor()

def get_logger(name, log_file, log_level="INFO"):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(msecs)d - %(funcName)s - %(lineno)d : %(levelname)s : %(message)s')
    fh = logging.FileHandler(filename=log_file)
    fh.setLevel(log_level)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def validate_params(endpoint, data):
    required_fields = cst.REQUIRED_FIELDS_MAP.get(endpoint)
    for field in required_fields:
        if data.get(field, None) is None:
            return False
    return True

def response(status, title, data={}, error={}):
    if cst.ENCRYPT_RESPONSE == True:
       data = encryptor.encrypt(json.dumps(data)).decode("utf-8")
    return json.dumps({
        "status": status,
        "title": title,
        "error": error,
        "data": data
    })