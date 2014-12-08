def NumberToSymbol(index):
    if index==0:
        return 'A'
    if index==1:
        return 'C'
    if index==2:
        return 'G'
    if index==3:
        return 'T'

def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = index/4
    r = index%4
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    symbol = NumberToSymbol(r)
    return PrefixPattern+symbol

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readlines()
index=int(s[0])
k=int(s[1])
a= NumberToPattern(index, k)
fout.write(str(a))
fin.close()
fout.close()