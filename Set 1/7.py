import base64
from Crypto.Cipher import AES
f = open("7.txt","rb")
b = base64.b64decode(f.readline().strip())
key = b"YELLOW SUBMARINE"
c = AES.new(key,AES.MODE_ECB)
print(c.decrypt(b))