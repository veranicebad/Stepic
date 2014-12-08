__author__ = 'Vera'
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s0=fin.readline().replace('\n','').split(' ')
s=fin.readline().replace('\n','')
k=int(s0[0])
d=int(s0[1])
reads=[]
for i in range(len(s)-2*k-d+1):
    r='('+s[i:i+k]+'|'+s[i+k+d:i+2*k+d]+')'
    reads.append(r)
reads.sort()
for r in reads:
    fout.write(str(r)+" ")
fin.close()
fout.close()
