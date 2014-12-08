import math
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
answer=[]
d=fin.readline().replace('\n','')
pr=fin.readline().replace('\n','')
print(d,pr)
s=[]
s1=[]
rcd=[]
for i in range(len(d)):
    s1.append(0)
    rcd.append(0)

for i in range(len(d)):
    if d[i]=='A':
        rcd[len(d)-1-i]='T'
    if d[i]=='C':
        rcd[len(d)-1-i]='G'
    if d[i]=='G':
        rcd[len(d)-1-i]='C'
    if d[i]=='T':
        rcd[len(d)-1-i]='A'

for i in range(len(d)):
    s.append(0)
for i in range(len(d)):
    if d[i]=='T':
        s[i]='U'
    else:
        s[i]=d[i]
for i in range(len(s)):
    if s[i]=='A':
        s1[len(s)-1-i]='U'
    if s[i]=='C':
        s1[len(s)-1-i]='G'
    if s[i]=='G':
        s1[len(s)-1-i]='C'
    if s[i]=='U':
        s1[len(s)-1-i]='A'
for j in range(3):
    mll=[]
    for i in range((len(s)-j)/3):
        mll.append('0')
        st = str(s[i*3+j])+str(s[i*3+1+j])+str(s[i*3+2+j])
        if(st=='UAA')or (st=='UAG')or (st=='UGA'):
            mll[i]='X'
        if (st=='AUG'):
            mll[i]='M'
        if (st=='UUU') or (st=='UUC'):
            mll[i]='F'
        if (st=='UUA') or (st=='UUG') or (st=='CUU')or (st=='CUC')or (st=='CUA')or (st=='CUG'):
            mll[i]='L'
        if (st=='UCU') or (st=='UCC') or (st=='UCA') or (st=='UCG'):
            mll[i]='S'
        if (st=='UAU') or (st=='UAC'):
            mll[i]='Y'
        if (st=='UGU') or (st=='UGC'):
            mll[i]='C'
        if(st=='UGG'):
            mll[i]='W'
        if (st=='CCU') or (st=='CCC') or (st=='CCA')or (st=='CCG'):
            mll[i]='P'
        if (st=='CAU') or (st=='CAC'):
            mll[i]='H'
        if (st=='CAA') or (st=='CAG'):
            mll[i]='Q'
        if (st=='CGU') or (st=='CGC') or (st=='CGA') or (st=='CGG')or (st=='AGA')or (st=='AGG'):
            mll[i]='R'
        if (st=='AUU') or (st=='AUC') or (st=='AUA'):
            mll[i]='I'
        if (st=='ACU') or (st=='ACC') or (st=='ACA') or (st=='ACG'):
            mll[i]='T'
        if (st=='AAU') or (st=='AAC'):
            mll[i]='N'
        if (st=='AAA') or (st=='AAG'):
            mll[i]='K'
        if (st=='AGU') or (st=='AGC'):
            mll[i]='S'
        if (st=='GUU') or (st=='GUC') or (st=='GUA') or (st=='GUG'):
            mll[i]='V'
        if (st=='GCU') or (st=='GCC') or (st=='GCA') or (st=='GCG'):
            mll[i]='A'
        if (st=='GAU') or (st=='GAC'):
            mll[i]='D'
        if (st=='GAA') or (st=='GAG'):
            mll[i]='E'
        if (st=='GGU') or (st=='GGC') or (st=='GGA') or (st=='GGG'):
            mll[i]='G'
        if (st!='UUU') and (st!='UUC')and (st!='UUA')and (st!='UUG')and (st!='UCU')and (st!='UCC')and (st!='UCA')and (st!='UCG')and (st!='UAU')and (st!='UAC')and (st!='UAA')and (st!='UAG')and (st!='UGU')and (st!='UGC')and (st!='UGA')and (st!='UGG')and (st!='CUU')and (st!='CUC')and (st!='CUA')and (st!='CUG')and (st!='CCU')and (st!='CCC')and (st!='CCA')and (st!='CCG')and (st!='CAU')and (st!='CAC')and (st!='CAA')and (st!='CAG')and (st!='CGU')and (st!='CGC')and (st!='CGA')and (st!='CGG')and (st!='AUU')and (st!='AUC')and (st!='AUA')and (st!='AUG')and (st!='ACU')and (st!='ACC')and (st!='ACA')and (st!='ACG')and (st!='AAU')and (st!='AAC')and (st!='AAA')and (st!='AAG')and (st!='AGU')and (st!='AGC')and (st!='AGA')and (st!='AGG')and (st!='GUU')and (st!='GUC')and (st!='GUA')and (st!='GUG')and (st!='GCU')and (st!='GCC')and (st!='GCA')and (st!='GCG')and (st!='GAU')and (st!='GAC')and (st!='GAA')and (st!='GAG')and (st!='GGU')and (st!='GGC')and (st!='GGA')and (st!='GGG'):
            print(st)
    print mll
    while(pr in ''.join(mll)):
        start_i = ''.join(mll).index(pr)
        print start_i
        print(d[start_i*3+j:start_i*3+j+len(pr)*3])
        answer.append(d[start_i*3+j:start_i*3+j+len(pr)*3])
        mll[start_i]='&'
        print mll
for j in range(3):
    mll1=[]
    for i in range((len(s1)-j)/3):
        mll1.append('0')
        st1 = str(s1[i*3+j])+str(s1[i*3+1+j])+str(s1[i*3+2+j])
        if(st1=='UAA')or (st1=='UAG')or (st1=='UGA'):
            mll1[i]='X'
        if (st1=='AUG'):
            mll1[i]='M'
        if (st1=='UUU') or (st1=='UUC'):
            mll1[i]='F'
        if (st1=='UUA') or (st1=='UUG') or (st1=='CUU')or (st1=='CUC')or (st1=='CUA')or (st1=='CUG'):
            mll1[i]='L'
        if (st1=='UCU') or (st1=='UCC') or (st1=='UCA') or (st1=='UCG'):
            mll1[i]='S'
        if (st1=='UAU') or (st1=='UAC'):
            mll1[i]='Y'
        if (st1=='UGU') or (st1=='UGC'):
            mll1[i]='C'
        if(st1=='UGG'):
            mll1[i]='W'
        if (st1=='CCU') or (st1=='CCC') or (st1=='CCA')or (st1=='CCG'):
            mll1[i]='P'
        if (st1=='CAU') or (st1=='CAC'):
            mll1[i]='H'
        if (st1=='CAA') or (st1=='CAG'):
            mll1[i]='Q'
        if (st1=='CGU') or (st1=='CGC') or (st1=='CGA') or (st1=='CGG')or (st1=='AGA')or (st1=='AGG'):
            mll1[i]='R'
        if (st1=='AUU') or (st1=='AUC') or (st1=='AUA'):
            mll1[i]='I'
        if (st1=='ACU') or (st1=='ACC') or (st1=='ACA') or (st1=='ACG'):
            mll1[i]='T'
        if (st1=='AAU') or (st1=='AAC'):
            mll1[i]='N'
        if (st1=='AAA') or (st1=='AAG'):
            mll1[i]='K'
        if (st1=='AGU') or (st1=='AGC'):
            mll1[i]='S'
        if (st1=='GUU') or (st1=='GUC') or (st1=='GUA') or (st1=='GUG'):
            mll1[i]='V'
        if (st1=='GCU') or (st1=='GCC') or (st1=='GCA') or (st1=='GCG'):
            mll1[i]='A'
        if (st1=='GAU') or (st1=='GAC'):
            mll1[i]='D'
        if (st1=='GAA') or (st1=='GAG'):
            mll1[i]='E'
        if (st1=='GGU') or (st1=='GGC') or (st1=='GGA') or (st1=='GGG'):
            mll1[i]='G'
        if (st1!='UUU') and (st1!='UUC')and (st1!='UUA')and (st1!='UUG')and (st1!='UCU')and (st1!='UCC')and (st1!='UCA')and (st1!='UCG')and (st1!='UAU')and (st1!='UAC')and (st1!='UAA')and (st1!='UAG')and (st1!='UGU')and (st1!='UGC')and (st1!='UGA')and (st1!='UGG')and (st1!='CUU')and (st1!='CUC')and (st1!='CUA')and (st1!='CUG')and (st1!='CCU')and (st1!='CCC')and (st1!='CCA')and (st1!='CCG')and (st1!='CAU')and (st1!='CAC')and (st1!='CAA')and (st1!='CAG')and (st1!='CGU')and (st1!='CGC')and (st1!='CGA')and (st1!='CGG')and (st1!='AUU')and (st1!='AUC')and (st1!='AUA')and (st1!='AUG')and (st1!='ACU')and (st1!='ACC')and (st1!='ACA')and (st1!='ACG')and (st1!='AAU')and (st1!='AAC')and (st1!='AAA')and (st1!='AAG')and (st1!='AGU')and (st1!='AGC')and (st1!='AGA')and (st1!='AGG')and (st1!='GUU')and (st1!='GUC')and (st1!='GUA')and (st1!='GUG')and (st1!='GCU')and (st1!='GCC')and (st1!='GCA')and (st1!='GCG')and (st1!='GAU')and (st1!='GAC')and (st1!='GAA')and (st1!='GAG')and (st1!='GGU')and (st1!='GGC')and (st1!='GGA')and (st1!='GGG'):
            print st1
    print mll1
    while(pr in ''.join(mll1)):
        start_i = ''.join(mll1).index(pr)
        print start_i
        print(d[len(d) - (start_i*3+j+len(pr)*3) : len(d) - (start_i*3+j)])
        answer.append(d[len(d) - (start_i*3+j+len(pr)*3) : len(d) - (start_i*3+j)])
        mll1[start_i]='&'
for i in range(len(answer)):
    fout.write(str(''.join(answer[i]))+str("\n"))
fin.close()
fout.close()