def LCSubStr(a,b):
    lena=len(a)
    lenb=len(b)
    LCS=[[0]*(lenb+1) for _ in range(lena+1)]
    for i in range(1,lena+1):
        for j in range(1,lenb+1):
            if a[i-1] == b[j-1] :
                LCS[i][j]=LCS[i-1][j-1]+1
            else:
                LCS[i][j]=max(LCS[i][j-1],LCS[i-1][j])
    return LCS



def LCSPrint(L,a,b,i,j):
    if i==0 or j==0:
        return set([""])
    elif a[i-1] == b[j-1] :
        return set([c+a[i-1] for c in LCSPrint(L,a,b,i-1,j-1)])
    else:
        R=set()
        if L[i][j-1] >= L[i-1][j]:
            R.update(LCSPrint(L, a, b, i, j-1))
        if L[i-1][j] >= L[i][j-1]:
            R.update(LCSPrint(L, a, b, i-1, j))
        return R

def emailid(email1,email2):
    email1=preprocess(email1)
    email2=preprocess(email2)
    L=LCSubstr(email1[0],email2[0])
    R=LCSPrint(L,email1[0],email2[0],len(email1[0]),len(email2[0]))