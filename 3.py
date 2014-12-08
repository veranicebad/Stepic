fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline()
for i in range(len(s)):
    if s[len(s)-1-i]=='T':
        fout.write('A')
    if s[len(s)-1-i]=='A':
        fout.write('T')
    if s[len(s)-1-i]=='C':
        fout.write('G')
    if s[len(s)-1-i]=='G':
        fout.write('C')
fin.close()
fout.close()
