__author__ = 'Vera'
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
s1=fin.readline().replace('\n','')
k=int(s1)
j=0
m=[[0 for x in range(k)] for x in range(4)]
for line in fin.readlines():
    ts=(line.replace('\n','').split(' '))
    for i in range(len(ts)):
        m[i][j]=float(ts[i])
    j+=1
maxscore=0
maxscorepattern=''
for e in range(len(s)-k+1):
    pattern=s[e:e+k]
    score=1
    for i in range(k):
        if pattern[i]=='A':
            score*=m[i][0]
        if pattern[i]=='C':
            score*=m[i][1]
        if pattern[i]=='G':
            score*=m[i][2]
        if pattern[i]=='T':
            score*=m[i][3]
    if maxscore<score:
        maxscore=score
        maxscorepattern=pattern
print(maxscorepattern)
fout.write(str(maxscorepattern))
fin.close()
fout.close()
