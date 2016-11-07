kb=["1234567890-=",  #Array Of Keyboard Keys
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./"]
skb=["!@#$%^&*()_+", #Same keys +Shift
     "QWERTYUIOP{}|",
     "ASDFGHJKL:\"",
     "ZXCVBNM<>?"]

keys={}
for i in range(len(kb)):
    for j in range(len(kb[i])):
        keys[kb[i][j]]=(i,j)

def dist(a,b):
    y1,x1=keys[a]
    y2,x2=keys[b]
    d=float(float((((x1-x2)**2)+((y1-y2)**2)))**(0.5))  #Euclidean Distance
    print d
