import base64
d = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
d_inv = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
def hamming(a,b):
    out = 0
    d = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
    d_inv = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
    ab = "".join([d[i] for i in a])
    bb = "".join([d[i] for i in b])
    for i in range(len(ab)):
        if ab[i%len(ab)]!=bb[i%len(bb)]:
            out+=1
    return out

# in1 = "this is a test".encode('utf-8').hex()
# in2 = "wokka wokka!!!".encode('utf-8').hex()

def xor(a,b): #b is shorter
    out = ""
    d = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
    ab = "".join([d[i] for i in a])
    bb = "".join([d[i] for i in b])
    for i in range(len(ab)):
        if ab[i]==bb[i%len(bb)]:
            out+="0"
        else:
            out+="1"
    d_inv = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
    return "".join([d_inv[out[i*4:i*4+4]] for i in range(len(out)//4)])

def score(x):
    count = 0
    for i in range(len(x)//2):
        if int(x[i*2:i*2+2],16) in range(97,123) or int(x[i*2:i*2+2],16) in range(65,91) or int(x[i*2:i*2+2],16)==32: #yeah i know it's shit
            count+=1
    return 2*count/len(x)

f = open("Set 1/6.txt","rb")
b = base64.b64decode(f.readline().strip())

minkey = 0
minsize = 10
for keysize in range(2,41):
    dis = sum([hamming(b[i*keysize:i*keysize+keysize].hex(),b[i*keysize+keysize:i*keysize+2*keysize].hex()) for i in range(500//keysize)])/(keysize*(500//keysize))
    if dis<minsize:
        minkey = keysize
        minsize = dis

byteblocks = [b'' for i in range(minkey)]
for i in range(len(b)):
    byteblocks[i%minkey]+=b[i].to_bytes(1,"big")

decblocks = []

for x in byteblocks:
    for i in range(256):
        xored = xor(x.hex(),hex(i)[2:])
        if score(xored)>0.85:
            decblocks.append(bytes.fromhex(xored))

print(len(decblocks))

out = b""
for i in range(len(decblocks[0])):
    for j in range(29):
        if len(decblocks[j])>i:
            out+=decblocks[j][i].to_bytes(1,"big")
print(out.decode('utf-8'))