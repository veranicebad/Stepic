import itertools

def SymbolToNumber(symbol):
    if symbol=='A':
        return 0
    if symbol=='C':
        return 1
    if symbol=='G':
        return 2
    if symbol=='T':
        return 3

def PatternToNumber(pattern):
        if len(pattern)==0:
            return 0
        symbol=pattern[len(pattern)-1]
        pattern=pattern[:len(pattern)-1]
        return 4*PatternToNumber(pattern) + SymbolToNumber(symbol)

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
a= PatternToNumber(s)
print a
fout.write(str(a))
fin.close()
fout.close()
