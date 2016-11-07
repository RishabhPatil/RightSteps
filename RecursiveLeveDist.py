def dstr(a,lena,b,lenb):
    cost = 0
    if lena==0:
        return lenb
    if lenb==0:
        return lena
    if a[lena-1]==b[lenb-1]:
        cost=0
    else:
        cost=1

    return min(dstr(a,lena-1,b,lenb)+1,
               dstr(a,lena,b,lenb-1)+1,
               dstr(a,lena-1,b,lenb-1)+cost)

def dstrc(a,b):
    return dstr(a.lower(),len(a),b.lower(),len(b))
