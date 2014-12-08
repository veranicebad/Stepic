import itertools
from operator import index
from sets import Set
def indexfinder(subs,s):
    pattern=subs
    index=[]
    d=1
    for i in range(len(s)-len(pattern)+1):
        t=0
        for j in range(len(pattern)):
            if not(s[i+j]==pattern[j]):
                t=t+1
            if t>d:
                break
        if t<=d:
            index.append(i)
    return index

def skewfinder(s):
    ans=0
    skew=[]
    skewmin=[]
    for i in range(len(s)):
        skew.append(ans)
        if s[i]=='G':
            ans=ans+1
        if s[i]=='C':
            ans=ans-1
    skew.append(ans)
    m=min(skew)
    for i in range(len(skew)):
        if(skew[i]==m):
            skewmin.append(i)
    return skewmin

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
all=''.join(fin.readlines()).replace('\n','')
genom=all[:len(all)-3]
s1=''.join(all[len(all)-3:]).replace('\n','').split(' ')
skewmin=skewfinder(genom)
mid=0
for i in range(len(skewmin)):
    mid=mid+skewmin[i]
mid=mid/len(skewmin)
print mid
l=160
s=genom[mid-l:mid+l+1]
print s
k=int(s1[0])
d=int(s1[1])

count={}
ans=[]
t=0

l1= list(itertools.combinations(range(0, k), d))
l2=list(itertools.product(['A','C','G','T'],repeat=d))
for e in range(len(s)-k+1):
    usedPatterns = Set()
    pattern=list(s[e:e+k])
    svp=pattern[:]
    for q in range(len(l1)):
        templist1=l1[q]
        for u in range(len(l2)):
            templist2=l2[u]
            for h in range(d):
                pattern[templist1[h]]=templist2[h]

            if ''.join(pattern) in usedPatterns:
                pattern=svp[:]
                continue
            usedPatterns.add(''.join(pattern))
            if ''.join(pattern) not in count:
                count[''.join(pattern)] = 1
            else:
                count[''.join(pattern)] = count[''.join(pattern)] + 1
            pattern=svp[:]

m=max(count.values())
for i in count.keys():
    if count[''.join(i)]==m:
        if not(i in ans):
            ans.append(i)
            fout.write(str(i)+' ')
    if count[''.join(i)] < m:
        count.pop(''.join(i))
print count
print ans
print ans[0],s,'\n'
print ans[0]
index=indexfinder(ans[0],s)
print index
dnaawindowstart=mid-l+index[0]
dnaawindowstop=mid-l+index[1]
print dnaawindowstart,dnaawindowstop
print genom[dnaawindowstart:dnaawindowstart+9],genom[dnaawindowstop:dnaawindowstop+9]
fout.write(str(dnaawindowstart)+' '+str(dnaawindowstop))
fin.close()
fout.close()