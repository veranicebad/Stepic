from copy import  deepcopy
import itertools
from sets import Set
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s1=fin.readline().split(' ')
k=int(s1[0])
strings=[]
for line in fin.readlines():
    strings.append(line.replace('\n',''))
print(strings)
count={}
ans=[]
t=0

def d_i(pattern, Dna_i):
    for d in range(0,len(pattern)+1):
        patternsWithdMM=getPatternsWithdMM(pattern,d)
        for p in patternsWithdMM:
            if p in Dna_i:
                return d


def getPatternsWithdMM(pattern, d):
    pattern=list(pattern)
    l1= list(itertools.combinations(range(0, len(pattern)), d))
    l2=list(itertools.product(['A','C','G','T'],repeat=d))
    usedPatterns = Set()
    svp=pattern[:]
    for q in range(len(l1)):
        templist1=l1[q]
        for u in range(len(l2)):
            flag=0
            templist2=l2[u]
            for h in range(d):
                if pattern[templist1[h]]!=templist2[h]:
                    pattern[templist1[h]]=templist2[h]
                else:
                    flag=1
            if (''.join(pattern) in usedPatterns) or (flag==1):
                pattern=svp[:]
                continue
            usedPatterns.add(''.join(pattern))
            pattern=svp[:]
    return usedPatterns


def d(pattern, Dna):
    sum=0
    for Dna_i in Dna:
        sum+=d_i(pattern, Dna_i)
    return(sum)

def getPatterns(k):
    l2=list(itertools.product(['A','C','G','T'],repeat=k))
    return l2

def MEDIANSTRING(Dna, k):
    patterns=getPatterns(k)
    BestPattern=patterns[0]
    for pattern in patterns:
        if d(pattern, Dna) < d(BestPattern, Dna):
             BestPattern = pattern
    return BestPattern

med=MEDIANSTRING(strings,k)
print(med)
fout.write(str(med))
fin.close()
fout.close()
