a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
d = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
b = "".join([d[i] for i in a])
out = ""
for i in range(len(b)//6):
    block = b[i*6:i*6+6]
    val = int(block,2)
    out+="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"[val]
print(out)