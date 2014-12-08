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


fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().split(' ')
number=int(s[0])
l=int(s[1])
print NumberToPattern(number, l)
fin.close()
fout.close()