import sys
from Crypto.Cipher import AES
from utils import expendString

password = expendString(sys.argv[1], 16)
iv = expendString(sys.argv[2], 16)

file = open(sys.argv[3], 'rb')
cipher = file.read()

obj = AES.new(password, AES.MODE_CBC, iv)
print(obj.decrypt(cipher))



