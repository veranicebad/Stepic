import itertools
from sets import Set
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
s1=fin.readline().split(' ')
k=int(s1[0])
d=int(s1[1])
count={}
ans=[]
t=0



l1= list(itertools.combinations(range(0, k), d))
l2=list(itertools.product(['A','C','G','T'],repeat=d))
for e in range(len(s)-k+1):
    usedPatterns = Set()
    pattern=list(s[e:e+k])
    svp=pattern[:]
    for q in range(len(l1)):
        templist1=l1[q]
        for u in range(len(l2)):
            templist2=l2[u]
            for h in range(d):
                pattern[templist1[h]]=templist2[h]

            if ''.join(pattern) in usedPatterns:
                pattern=svp[:]
                continue
            usedPatterns.add(''.join(pattern))
            if ''.join(pattern) not in count:
                count[''.join(pattern)] = 1
            else:
                count[''.join(pattern)] = count[''.join(pattern)] + 1
            pattern=svp[:]

m=max(count.values())
for i in count.keys():
    if count[''.join(i)]==m:
        if not(i in ans):
            ans.append(i)
            fout.write(str(i)+' ')
    if count[''.join(i)] < 10:
        count.pop(''.join(i))
print count
print ans,'!'
fin.close()
fout.close()
