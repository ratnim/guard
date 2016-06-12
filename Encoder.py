from Crypto.Cipher import AES

class Encoder:
    """"Simple Proxy for Crypto.Cipher"""

    @staticmethod
    def extent_string_to_base(string, base):
        while len(string) % base:
            string += ' '
        return string

    @staticmethod
    def encode(password, iv, content):
        filled_password = Encoder.extent_string_to_base(password, 16)
        filled_iv = Encoder.extent_string_to_base(iv, 16)
        filled_content = Encoder.extent_string_to_base(content, 16)
        obj = AES.new(filled_password, AES.MODE_CBC, filled_iv)
        return obj.encrypt(filled_content)

    @staticmethod
    def decode(password, iv, content):
        filled_password = Encoder.extent_string_to_base(password, 16)
        filled_iv = Encoder.extent_string_to_base(iv, 16)

        obj = AES.new(filled_password, AES.MODE_CBC, filled_iv)
        return obj.decrypt(content)