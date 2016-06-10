import sys
from Crypto.Cipher import AES
from utils import extend_string_to_base

password = extend_string_to_base(sys.argv[1], 16)
iv = extend_string_to_base(sys.argv[2], 16)

file = open(sys.argv[3], 'rb')
cipher = file.read()

obj = AES.new(password, AES.MODE_CBC, iv)
print(obj.decrypt(cipher))



