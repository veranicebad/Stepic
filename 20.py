from sets import Set
N=Set()
N.add('A')
N.add('C')
N.add('G')
N.add('T')

def HammingDistance(s1, s2):
    ans=0
    for i in range(len(s1)):
        if not(s1[i]==s2[i]):
            ans=ans+1
    return ans

def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern)== 1:
        return N
    Neighborhood=[]
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], text) < d:
            for x in N:
                Neighborhood.append(x + text)
        else:
            Neighborhood.append(Pattern[0] + text)
    return Neighborhood

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
s1=fin.readline()
d=int(s1[0])
a= Neighbors(s,d)
for i in range(len(a)):
    fout.write(str(a[i])+'\n')
fin.close()
fout.close()