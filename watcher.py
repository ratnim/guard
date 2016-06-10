import sys
from Crypto.Cipher import AES

def expendString( string, base ):
	"Expends until it is a multiple of base"
	fit = len( string ) % base  
	if (fit == 0):
		return string
	for i in range(base - fit):
		string += ' '
	return string

password = expendString(sys.argv[1], 16)
iv = expendString(sys.argv[2], 16)

file = open(sys.argv[3], 'rb')
cipher = file.read()

obj = AES.new(password, AES.MODE_CBC, iv)
print(obj.decrypt(cipher))



