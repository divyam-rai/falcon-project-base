import os
import sys
sys.path.append(os.getenv('BASEPATH'))

from utils import constants as cst
from Crypto import Random
from Crypto.Cipher import AES
import base64

class Encryptor:
    def __init__(self):
        self.key = "{: <32}".format(cst.ENCRYPTION_KEY).encode("utf-8")

    def encrypt(self, data):
        raw = self._pad(data)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv, segment_size=128)
        return base64.b64encode(iv + cipher.encrypt(raw))
    
    def decrypt(self, data):
        enc = base64.b64decode(data)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
    
    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]