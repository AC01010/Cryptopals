def xor(a,b):
    out = ""
    d = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
    ab = "".join([d[i] for i in a])
    bb = "".join([d[i] for i in b])
    for i in range(len(ab)):
        if ab[i%len(ab)]==bb[i%len(bb)]:
            out+="0"
        else:
            out+="1"
    d_inv = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
    return "".join([d_inv[out[i*4:i*4+4]] for i in range(len(out)//4)])

in1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
print(xor(in1.encode('utf-8').hex(),"ICE".encode('utf-8').hex()))

def score(x):
    count = 0
    for i in range(len(x)//2):
        if int(x[i*2:i*2+2],16) in range(97,123) or int(x[i*2:i*2+2],16) in range(65,91) or int(x[i*2:i*2+2],16)==32:
            count+=1
    return 2*count/len(x)