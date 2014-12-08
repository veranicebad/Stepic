fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
pattern=fin.readline().replace('\n','')
d=int(fin.readline())
count=0
for i in range(len(s)-len(pattern)+1):
    t=0
    for j in range(len(pattern)):
        if not(s[i+j]==pattern[j]):
            t=t+1
        if t>d:
            break
    if t<=d:
        count=count+1
fout.write(str(count))
fin.close()
fout.close()
