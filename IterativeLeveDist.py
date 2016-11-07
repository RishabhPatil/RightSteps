def dist(a,b):
    if a==b:
        return 0
    if len(a)==0:
        return len(b)
    if len(b)==0:
        return len(a)
    v0=[i for i in range(len(a)+1)]
    v1=[0 for i in range(len(a)+1)]
    for i in range(len(b)):
        v1[0]=i+1
        for j in range(len(a)):
            cost=0
            if b[i]==a[j]:
                cost=0
            else:
                cost=1
            v1[j+1]=min(v1[j]+1,v0[j+1]+1,v0[j]+cost)
        for j in range(len(v0)):
            v0[j]=v1[j]
    return v1[len(a)]

print dist("asdfg","sdfgh")
