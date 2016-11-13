import re

def compare(t,n):
        c=0
        k='y'
        if data[n]:
                for i in data[n]:
                        for j in range(len(i)):
                                if i[j]==t[j]:
                                        c=c+1
                        if c==4:
                                k='n'
        if k=='y':
                data[n].append(tuple(t))

data=[list() for i in range(27)]
print data
#Read from CSV
with open('data.csv', 'rb') as f:
        df=f.read()
        df=df.split("\n")
        for i in df:
#Cleanse Data
                i=re.sub('\\r','',i)
                t=i.split(',')
                j=27
                t[0]=(t[0].lstrip()).rstrip()
                if len(t[0])!=0:
                        j=ord(t[0][0].lower())-97
                else:
                        j=26
                t[0]=re.sub('[^a-z ]+','',t[0].lower())             #[1][2]
                t[0]=t[0].split(' ')
                t[1]=t[1].lower()
                t[1]=t[1].split('@')
                t[2]=re.sub('[^0-9]+','',t[2].lower())             #[3][4]
                t[3]=t[3].lower()
                t[3]=t[3].split(' ')
#Compare with group based on 1st alphabet
                compare(t,j)

"""
FINAL FORMAT:
(['tejas', 'dhanepkar'], ['tejasdhanepkar25', 'gmail.com'], '7038810983', ['428', 'kearsley', 'st'])
"""

for i in range(27):
        print data[i]

"""
ISSUES:
[1] RE support for all languages (Unicode) : http://stackoverflow.com/questions/7206499/
[2] Current RE replaces '-' with '' so hyphenated strings are appended. Other similar issues?
[3] Phone numbers with calling codes? Split on 1st ' ' after '+'?
[4] Calling codes are always prefixes, so we can compare in reverse order?
"""
