fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
pattern=fin.readline().replace('\n','')
s=fin.readline().replace('\n','')
d=int(fin.readline())
for i in range(len(s)-len(pattern)+1):
    t=0
    for j in range(len(pattern)):
        if not(s[i+j]==pattern[j]):
            t=t+1
        if t>d:
            break
    if t<=d:
        print i
        fout.write(str(i)+' ')
fin.close()
fout.close()
