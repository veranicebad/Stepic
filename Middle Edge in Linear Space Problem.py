def Ss(v, w):
    global sigma
    global score
    m=len(v)+1
    n=len(w)+1
    s_prev=[0 for x in range(n)]
    s=[0 for x in range(n)]
    s[0]=-sigma
    for j in range(n):
        s_prev[j] = -sigma*j
    for j in range(1,len(v) + 1):
        s[0] = -sigma*j
        for i in range(1,len(w) + 1):
            f=score[alp[v[j-1]]][alp[w[i-1]]]
            s[i] = max(s[i-1]-sigma, s_prev[i]-sigma, s_prev[i-1] + f)
        s_prev=s[:]
    return(s)

fin = open('input.txt', 'r')
fin2 = open('alp.txt', 'r')
fout=open('output.txt', 'w')
v_y=fin.readline().replace('\n','')
w_y=fin.readline().replace('\n','')
alp={}
a=fin2.readline().replace('  ',' ').replace('\n','').replace('  ','').split(' ')
i=0

for symb in a:
    alp[symb]=i
    i=i+1
score=[]
for line in fin2.readlines():
    st=line.replace('\n','').replace('  ',' ').split(' ')
    score.append([int(a) for a in st[1:]])
w=v_y[::]
v=w_y[::]
mi=(len(v)+2)/2
print(mi,'---')
sigma = 5
x1=0
y1=mi-1
x2=0
y2=mi
w1=w[::]
w2=w[::]
v1=v[::]
v2=v[::]
w2=w2[::-1]
v1=v1[:mi - 1]
v2=v2[mi:][::-1]
#v1=v1[:mi]
#v2=v2[mi+1:][::-1]
s1=Ss(v1,w1)
s2=Ss(v2,w2)
print(v2,w2)
print(s1,s2)
s2.append(-10000)
s2=s2[::-1]
s_max=s1[0]+s2[0]-sigma
for i in range(1,len(w)):
    if s_max<s1[i]+s2[i]-sigma:
        s_max=s1[i]+s2[i]-sigma
        x1=i
        x2=i
    f=score[alp[v[mi-1]]][alp[w[i-1]]]
    if s_max<s1[i-1]+s2[i]+f:
        s_max=s1[i-1]+s2[i]+f
        x1=i-1
        x2=i
print(x1,y1,x2,y2)
print(len(v))
fout.write('('+str(x1)+', '+str(y1)+') '+'('+str(x2)+', '+str(y2)+')')
