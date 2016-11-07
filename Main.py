from IterativeLeveDist import dist

def cfn(a,b):
    a=a.split(" ")
    b=b.split(" ")
    return min( dist(a[0],b[0])+dist(a[len(a)-1],b[len(b)-1]),
                dist(a[len(a)-1],b[0])+dist(a[0],b[len(b)-1]) )

records=0
data=[]
with open('1.csv','r') as f:
    datafull=f.read()
    datarecords=datafull.split('\n')
    records=len(datarecords)
    for i in range(records):
        data.append(datarecords[i].split(','))
        
for i in range(1,records):
    for j in range(i+1,records):
        dis=cfn(data[i][0],data[j][0])
        if dis<7:
            print data[i][0]," ",data[j][0],"->",cfn(data[i][0],data[j][0])
