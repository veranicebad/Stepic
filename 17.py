import itertools

def PatternToNumber(pattern):
    l=len(pattern)
    dpn={}
    l2=list(itertools.product(['A','C','G','T'],repeat=l))
    for i in range(len(l2)):
       dpn[str(l2[i]).replace('(','').replace(')','').replace(", ", '').replace("'",'')]=i
    return dpn[pattern]


def NumberToPattern(number, l):
    dpn={}
    l2=list(itertools.product(['A','C','G','T'],repeat=l))
    for i in range(len(l2)):
       dpn[str(l2[i]).replace('(','').replace(')','').replace(", ", '').replace("'",'')]=i
    return dpn.keys()[dpn.values().index(number)]

def cF(s, k):
    FrequencyArray=[]
    for i in range(4**k):
        FrequencyArray.append(0)
    for i in range(len(s)-k+1):
        pattern=s[i:i+k]
        j=PatternToNumber(pattern)
        FrequencyArray[j]=FrequencyArray[j] + 1
    return FrequencyArray


fin = open('input.txt', 'r')
fout=open('output.txt', 'w')

s=fin.readline().replace('\n','')
s1=fin.readline().split(' ')
k=int(s1[0])
a= cF(s,k)
for i in range(len(a)):
    fout.write(str(a[i])+' ')
fin.close()
fout.close()
