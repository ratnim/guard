import sys
from Crypto.Cipher import AES
from utils import extend_string_to_base

password = extend_string_to_base(sys.argv[1], 16)
iv = extend_string_to_base(sys.argv[2], 16)

source_file = open(sys.argv[3], 'r')

input = extend_string_to_base(source_file.read(), 16)

print( input )

obj = AES.new(password, AES.MODE_CBC, iv)
cipher = obj.encrypt(input)
print(cipher)

file = open(sys.argv[3].split('.')[0], 'wb')
file.write(cipher)