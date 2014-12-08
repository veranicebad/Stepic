import itertools

def PatternToNumber(pattern):
    l=len(pattern)
    dpn={}
    #l1= list(itertools.combinations(range(0, k), l))
    l2=list(itertools.product(['A','C','G','T'],repeat=l))
    for i in range(len(l2)):
       dpn[str(l2[i]).replace('(','').replace(')','').replace(", ", '').replace("'",'')]=i
    return dpn[pattern]


fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')

print PatternToNumber(s)
fin.close()
fout.close()