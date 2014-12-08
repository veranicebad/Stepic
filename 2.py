import operator
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
k=int(fin.readline())
d={}
for i in range(len(s)):
    if s[i:i+k] in d:
        d[s[i:i+k]]=d[s[i:i+k]]+1
    else:
        d[s[i:i+k]]=1
print d
m=max(d.values())
#max(d.iteritems(), key=operator.itemgetter(1))[0]
print m
for key, value in d.items():
    if value==m:
        print key
        fout.write(str(key)+' ')
fin.close()
fout.close()
