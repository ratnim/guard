from Crypto.Cipher import AES
from utils import extent_string_to_base

class Encoder:
    """"Simple Proxy for Crypto.Cipher"""

    @staticmethod
    def encode(password, iv, content):
        filled_password = extent_string_to_base(password, 16)
        filled_iv = extent_string_to_base(iv, 16)
        filled_content = extent_string_to_base(content, 16)
        obj = AES.new(filled_password, AES.MODE_CBC, filled_iv)
        return obj.encrypt(filled_content)

    @staticmethod
    def decode(password, iv, content):
        filled_password = extent_string_to_base(password, 16)
        filled_iv = extent_string_to_base(iv, 16)

        obj = AES.new(filled_password, AES.MODE_CBC, filled_iv)
        return obj.decrypt(content)