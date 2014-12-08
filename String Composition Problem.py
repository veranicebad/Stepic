__author__ = 'Vera'
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s0=fin.readline().replace('\n','').split(' ')
s=fin.readline().replace('\n','')
k=int(s0[0])
reads=[]
for i in range(len(s)-k+1):
    r=s[i:i+k]
    reads.append(r)
reads.sort()
for r in reads:
    fout.write(str(r)+"\n")
fin.close()
fout.close()
