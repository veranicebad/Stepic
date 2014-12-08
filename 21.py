from __future__ import division
from sets import Set
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
N=Set()
N.add('A')
N.add('C')
N.add('G')
N.add('T')
a=(1/4)**9
print a
fout.write(str(a))
fin.close()
fout.close()