__author__ = 'Vera'
__author__ = 'Vera'
from sets import Set
from copy import  deepcopy
import itertools
from random import *

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s0=fin.readline().replace('\n','').split(' ')
k=int(s0[0])
t=int(s0[1])
N=int(s0[2])
strings=[]

for line in fin.readlines():
    strings.append(line.replace('\n',''))

def Profile(Motifs):
    profile=[[0 for x in range(k)] for x in range(255)]
    for i in range(len(Motifs[0])):
        d={'A':0,'C':0, 'G':0,'T':0}
        for j in range(len(Motifs)):
            if Motifs[j][i] in d:
                d[Motifs[j][i]]+=1
            else:
                d[Motifs[j][i]]=1
        for key, value in d.items():
            profile[ord(key)][i]=float(value+1)/float(len(Motifs)+4)
    return(profile)


def findBestMotiff(s,Profile):
    maxscore=0.0
    maxscorepattern=s[:k]
    for e in range(len(s)-k+1):
        pattern=s[e:e+k]
        score=1.0
        for i in range(k):
            score*=Profile[ord(pattern[i])][i]
        if maxscore<score:
            maxscore=score
            maxscorepattern=pattern
    return(maxscorepattern)

def Score(Motifs):
    score=len(Motifs)*len(Motifs[0])
    for i in range(len(Motifs[0])):
        d={}
        for j in range(len(Motifs)):
            if Motifs[j][i] in d:
                d[Motifs[j][i]]+=1
            else:
                d[Motifs[j][i]]=1
        score-=max(d.values())
    return(score)

def RandomMotifs(k,Dna):
    Motifs=[]
    for i in range(len(Dna)):
        r=randint(0,len(Dna[0])-k)
        Motifs.append(Dna[i][r:r+k])
    return(Motifs)

def GibbssRandom(s, profile):
    p=[]
    for e in range(len(s)-k+1):
        pattern=s[e:e+k]
        p.append(1.0)
        for i in range(k):
            p[e]*=profile[ord(pattern[i])][i]
    sum2=0.0
    for i in range(len(s)-k+1):
        sum2+=p[i]
    for i in range(len(s)-k+1):
        p[i]/=sum2
    r=random()
    func_r=0
    for i in range(len(s)-k+1):
        func_r+=p[i]
        if(r<func_r):
            return i

def GIBBSSAMPLER(Dna,N):
    Motifs = RandomMotifs(k,Dna)
    BestMotifs = Motifs
    for j in range(N):
        i = randint(0,t-1)
        Motifs_exc_mi=Motifs[:]
        #print(i)
        Motifs_exc_mi.remove(Motifs_exc_mi[i])
        profile=Profile(Motifs_exc_mi)
        r=GibbssRandom(Dna[i],profile)
        #print(r)
        Motifs[i] = Dna[i][r:r+k]
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
mscore=10000
BestMotifs = []
for i in range(20):
    Motifs=GIBBSSAMPLER(strings,N)
    sc=Score(Motifs)
    if sc < mscore:
            BestMotifs = Motifs
            mscore=sc
            print(sc)
for m in BestMotifs:
    fout.write(str(m)+'\n')