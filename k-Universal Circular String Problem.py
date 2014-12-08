from random import randint
import itertools
__author__ = 'Vera'
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
smegnosty={}
#reverse_smegnosty={}
count_us = 0
count = 0
used={}
cycle=[]
#count_e=1
count_e=0
s1=fin.readline().replace('\n','')
k=int(s1)
reads=[]
reads= [''.join(list(r)) for r in list(itertools.product(['0','1'], repeat=k))]
patterns=[]
for r in reads:
    prefix=r[:-1]
    suffix=r[1:]
    if not(prefix in patterns):
        patterns.append(prefix)
    if not(suffix in patterns):
        patterns.append(suffix)
for pattern in patterns:
    smegnosty[pattern]=[]
for r in reads:
    smegnosty[r[:-1]].append(r[1:])

for v in smegnosty.keys():
#    list_temp=smegnosty[v]
#    for v1 in list_temp:
#        if v1 in reverse_smegnosty.keys():
#            reverse_smegnosty[v1].append(v)
#        else:
#            reverse_smegnosty[v1]=[]
#            reverse_smegnosty[v1].append(v)
    count_e=count_e+len(smegnosty[v])
    used[v]=[]


def formCycle(v0):
    global count_us, count_e
    cycle=[]
    cycle.append(v0)
    r=randint(0,len(smegnosty[v0])-1)
    v1=smegnosty[v0][r]
    while(v1 in used[v0]):
        r=randint(0,len(smegnosty[v0])-1)
        v1=smegnosty[v0][r]
    used[v0].append(v1)
    count_us+=1
    if v1==v0:
        return cycle
    else:
        cycle.append(v1)
    while True:
        r=randint(0,len(smegnosty[v1])-1)
        while(smegnosty[v1][r] in used[v1]):
            r=randint(0,len(smegnosty[v1])-1)
        v0=v1
        v1=smegnosty[v1][r]
        used[v0].append(v1)
        count_us=count_us+1
        if v1==cycle[0]:
            return cycle
        else:
            cycle.append(v1)

def newStart(cycle):
    for v in cycle:
        if not(len(used[v])==len(smegnosty[v])):
            return v

def EULERIANCYCLE(v0):
        cycle=formCycle(v0)
        while not(count_us==count_e):
            v0=newStart(cycle)
            cycle2=formCycle(v0)
            i=0
            for v in cycle:
                if v==v0:
                    i=cycle.index(v)
                    break
            cycle=(cycle[:i]+cycle2[:]+cycle2[:1]+cycle[i+1:])
        cycle.append(cycle[0])
        return cycle
#start=0
#stop=0
print(smegnosty)
#for v in smegnosty.keys():
#    if v not in reverse_smegnosty:
#        reverse_smegnosty[v] = []
#    if len(smegnosty[v])>len(reverse_smegnosty[v]):
#        start=v
#    if len(smegnosty[v])<len(reverse_smegnosty[v]):
#        stop=v
#for v in reverse_smegnosty.keys():
#    if v not in smegnosty:
#        smegnosty[v] = []
#    if len(smegnosty[v])>len(reverse_smegnosty[v]):
#        start=v
#    if len(smegnosty[v])<len(reverse_smegnosty[v]):
#        stop=v
#print(start,stop)
#for v in smegnosty.keys():
#    if smegnosty[v]==[]:
#        smegnosty.pop(v,None)

#if stop in smegnosty.keys():
#    smegnosty[stop].append(start)
#else:
#    smegnosty[stop]=[]
#    smegnosty[stop].append(start)
#used[stop]=[]
r=randint(0,len(smegnosty.keys())-1)
v0=smegnosty.keys()[r]

cycle=(EULERIANCYCLE(v0))
#cycle=cycle[1:]
#i=cycle.index(start, 0)

#while cycle[i-1]!=stop:
#    i=cycle.index(start, i+1)

path=cycle[:-1]
print(path)
fout.write(path[0])
for p in path[1:-k+2]:
    fout.write(p[-1])
fin.close()
fout.close()
