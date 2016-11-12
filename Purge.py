import csv

def compare(t,n):
	c=0
	k='y'
	for i in data[n]:
		for j in range(len(i)):
			if i[j]==t[j]:
				c=c+1
		if c>2:
			print t,i
			#k=raw_input("Add new?")
			break # RETURN SOMETHING MAYBE???
	if k=='y':
		data[n].add(tuple(t))

data=[set() for i in range(27)]
with open('data.csv', 'rb') as f:
	df=f.read()
	df=df.split("\n")
	for i in df:
		t=i.split(',')
		if len(t[0])!=0:
			t[0]=t[0].lstrip()
			j=ord(t[0][0].lower())-97
			compare(t,j)
		else:
			compare(t,26)
		#x=raw_input()

# (Name:{Yash Kale, YK},PH:{23443},EMAIL:{23vcc0},ADD:{asdafaf, asd})
for i in range(27):
	print data[i]
