from __future__ import division
from sets import Set
import math
from math import factorial
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
n=25
k=2
a=2
ans=factorial(476)/(factorial(3)*factorial(473))
fout.write(str(ans))
print ans

fin.close()
fout.close()