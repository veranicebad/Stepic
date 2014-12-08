fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s1=fin.readline().replace('\n','')
s2=fin.readline().replace('\n','')
ans=0
for i in range(len(s1)):
    if not(s1[i]==s2[i]):
        ans=ans+1
print ans
fout.write(str(ans))
fin.close()
fout.close()
