fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
ans=0
skew=[]
for i in range(len(s)):
    skew.append(ans)
    #print ans
    #fout.write(str(ans)+' ')
    if s[i]=='G':
        ans=ans+1
    if s[i]=='C':
        ans=ans-1
#print ans
skew.append(ans)
m=min(skew)
for i in range(len(skew)):
    if(skew[i]==m):
        print i
        fout.write(str(i)+' ')
fin.close()
fout.close()
