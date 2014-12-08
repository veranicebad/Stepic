fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
ans=0
for i in range(len(s)):
    print ans
    fout.write(str(ans)+' ')
    if s[i]=='G':
        ans=ans+1
    if s[i]=='C':
        ans=ans-1
print ans
fout.write(str(ans))
fin.close()
fout.close()
