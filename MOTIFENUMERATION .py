from copy import  deepcopy
import itertools
from sets import Set
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s1=fin.readline().split(' ')
k=int(s1[0])
d=int(s1[1])
strings=[]
for line in fin.readlines():
    strings.append(line.replace('\n',''))
print(strings)
count={}
ans=[]
t=0

def getPatterns(s):
    l1= list(itertools.combinations(range(0, k), d))
    l2=list(itertools.product(['A','C','G','T'],repeat=d))
    usedPatterns = Set()
    for e in range(len(s)-k+1):
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
                pattern=svp[:]
    return usedPatterns

patternsS0=getPatterns(strings[0])
#ans=deepcopy(patternsS0)
for p in patternsS0:
    temp=0
    for s2 in strings[1:]:
        #print(p,'66', getPatterns(s2))
        if not(p in getPatterns(s2)):
            break
            #ans.remove(p)
        else:
            temp+=1
    if temp==len(strings)-1:
        print(p)
        fout.write(p+' ')
fin.close()
fout.close()
