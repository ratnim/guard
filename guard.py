import sys
from Crypto.Cipher import AES
from utils import expendString

password = expendString(sys.argv[1], 16)
iv = expendString(sys.argv[2], 16)

source_file = open(sys.argv[3], 'r')

input = expendString(source_file.read(), 16)

print( input )

obj = AES.new(password, AES.MODE_CBC, iv)
cipher = obj.encrypt(input)
print(cipher)

file = open(sys.argv[3].split('.')[0], 'wb')
file.write(cipher)


