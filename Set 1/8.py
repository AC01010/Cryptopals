f = open("8.txt","rb")
for i in range(204):
    l = f.readline().strip().decode('utf-8')
    s = set([l[i*16:i*16+16] for i in range(20)])
    if len(s)<20:
        print(l)