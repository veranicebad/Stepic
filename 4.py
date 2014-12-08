import math
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
t=fin.readlines()
subs=str(t[0]).replace('\n','')
s=str(t[1]).replace('\n','')
ans=[]
while subs in s:
    i=s.find(subs)
    ans.append(i)
    s=s[:i]+'%'+s[i+1:]
print ans
for i in range(len(ans)):
    fout.write(str(ans[i])+' ')
fin.close()
fout.close()
