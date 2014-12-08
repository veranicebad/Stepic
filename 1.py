import math
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
t=fin.readlines()
subs=str(t[0]).replace('\n','')
s=str(t[1]).replace('\n','')
count=0
while subs in s:
    i=s.find(subs)
    count=count+1
    s=s[:i]+'%'+s[i+1:]
fout.write(str(count)+' ')
fin.close()
fout.close()
