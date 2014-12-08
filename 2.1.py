__author__ = 'Vera'
import math
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline()
i=0
ans=''
print len(s)
for i in range(len(s)/3):
    st = str(s[i*3])+str(s[i*3+1])+str(s[i*3+2])
    if (st=='UUU') or (st=='UUC'):
        ans=ans+'F'
    if (st=='UUA') or (st=='UUG') or (st=='CUU')or (st=='CUC')or (st=='CUA')or (st=='CUG'):
        ans=ans+'L'
    if (st=='UCU') or (st=='UCC') or (st=='UCA') or (st=='UCG'):
        ans=ans+'S'
    if (st=='UAU') or (st=='UAC'):
        ans=ans+'Y'
    if (st=='UGU') or (st=='UGC'):
        ans=ans+'C'
    if(st=='UGG'):
        ans=ans+'W'
    if (st=='CCU') or (st=='CCC') or (st=='CCA')or (st=='CCG'):
        ans=ans+'P'
    if (st=='CAU') or (st=='CAC'):
        ans=ans+'H'
    if (st=='CAA') or (st=='CAG'):
        ans=ans+'Q'
    if (st=='CGU') or (st=='CGC') or (st=='CGA') or (st=='CGG')or (st=='AGA')or (st=='AGG'):
        ans=ans+'R'
    if (st=='AUU') or (st=='AUC') or (st=='AUA'):
        ans=ans+'I'
    if (st=='AUG'):
        ans=ans+'M'
    if (st=='ACU') or (st=='ACC') or (st=='ACA') or (st=='ACG'):
        ans=ans+'T'
    if (st=='AAU') or (st=='AAC'):
        ans=ans+'N'
    if (st=='AAA') or (st=='AAG'):
        ans=ans+'K'
    if (st=='AGU') or (st=='AGC'):
        ans=ans+'S'
    if (st=='GUU') or (st=='GUC') or (st=='GUA') or (st=='GUG'):
        ans=ans+'V'
    if (st=='GCU') or (st=='GCC') or (st=='GCA') or (st=='GCG'):
        ans=ans+'A'
    if (st=='GAU') or (st=='GAC'):
        ans=ans+'D'
    if (st=='GAA') or (st=='GAG'):
        ans=ans+'E'
    if (st=='GGU') or (st=='GGC') or (st=='GGA') or (st=='GGG'):
        ans=ans+'G'
fout.write(str(ans))
fin.close()
fout.close()
