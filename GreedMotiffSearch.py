__author__ = 'Vera'
from sets import Set
from copy import  deepcopy
import itertools

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s0=fin.readline().replace('\n','').split(' ')
k=int(s0[0])
t=int(s0[1])
strings=[]
for line in fin.readlines():
    strings.append(line.replace('\n',''))

def Profile(Motifs):

    profile=[[0 for x in range(k)] for x in range(255)]
    for i in range(len(Motifs[0])):
        d={}
        for j in range(len(Motifs)):
            if Motifs[j][i] in d:
                d[Motifs[j][i]]+=1
            else:
                d[Motifs[j][i]]=1
        for key, value in d.items():
            profile[ord(key)][i]=float(value)/float(len(Motifs))
    return(profile)


def findBestMotiff(s,m):
    maxscore=0.0
    maxscorepattern=s[:k]
    for e in range(len(s)-k+1):
        pattern=s[e:e+k]
        score=1.0
        for i in range(k):
            score*=m[ord(pattern[i])][i]


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

def GREEDYMOTIFSEARCH(Dna, k,t):
    BestMotifs=[]

    for i in Dna:
        BestMotifs.append(i[:k])
    for e in range(len(Dna[0])-k+1):
        Motif=(Dna[0][e:e+k])
        Motif1 = Motif
        Motifs=[]
        Motifs.append(Motif1)
        for i  in range(1,t):
            profile=Profile(Motifs)
            Motifi=findBestMotiff(Dna[i],profile)
            Motifs.append(Motifi)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    for bm in BestMotifs:
        print(bm)


GREEDYMOTIFSEARCH(strings, k, t)
