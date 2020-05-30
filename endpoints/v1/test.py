import os
import sys
sys.path.append(os.getenv('BASEPATH'))

import falcon
from utils import constants as cst, general as hp

logger = hp.get_logger("test_endpoint", cst.LOGGER["test_endpoint"])

class Test():
    def on_get(self, res, resp):
        resp.body = hp.response(200, "SUCCESS", {'name' : 'Divyam'}, {})