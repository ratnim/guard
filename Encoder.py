import sys
from Crypto.Cipher import AES
from utils import extend_string_to_base

class Encoder:
    """"Simple Proxy for Crypto.Cipher"""

    @staticmethod
    def encode(self, password, iv, content):
        password = extend_string_to_base(password, 16)
        iv = extend_string_to_base(iv, 16)

        content = extend_string_to_base(content, 16)

        obj = AES.new(password, AES.MODE_CBC, iv)
        return obj.encrypt(input)

    @staticmethod
    def decode(self, password, iv, content):
        password = extend_string_to_base(password, 16)
        iv = extend_string_to_base(iv, 16)

        obj = AES.new(password, AES.MODE_CBC, iv)
        return obj.decrypt(content)