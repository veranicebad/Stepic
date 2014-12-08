def LCSBACKTRACK(v, w):
    sc=0
    sigma=11
    eps=1
    global  score
    print(v,w)
    m=len(v)+1
    n=len(w)+1
    Backtrack_l=[[0 for x in range(m)]for y in range(n)]
    Backtrack_u=[[0 for x in range(m)]for y in range(n)]
    Backtrack_m=[[0 for x in range(m)]for y in range(n)]
    lower=[[0 for x in range(m)]for y in range(n)]
    upper=[[0 for x in range(m)]for y in range(n)]
    middle=[[0 for x in range(m)]for y in range(n)]
    for i in range(n):
        lower[i][0]=-eps*i
        upper[i][0]=0
        middle[i][0]=0
        Backtrack_l[i][0] =0
    for j in range(m):
        lower[i][0]=0
        upper[i][0]=-eps*j
        middle[i][0]=0
        Backtrack_u[0][j] = 0
    for i in range(1,len(w) + 1):
        for j in range(1,len(v) + 1):
            f=score[alp[v[j-1]]][alp[w[i-1]]]
            lower[i][j]= max(lower[i-1][j]-eps, middle[i-1][j]-sigma)
            upper[i][j]=max(upper[i][j-1]-eps, middle[i][j-1]-sigma)
            middle[i][j]=max(lower[i][j], upper[i][j], middle[i-1][j-1]+f)
            if lower[i][j] == lower[i-1][j]-eps:
                Backtrack_l[i][j] = 0
            if lower[i][j] == middle[i-1][j]-sigma:
                Backtrack_l[i][j] = 1
            if upper[i][j] == upper[i][j-1]-eps:
                Backtrack_u[i][j] = 0
            if lower[i][j] == middle[i][j-1]-sigma:
                Backtrack_u[i][j] = 1
            if middle[i][j] == lower[i][j]:
                Backtrack_m[i][j]= 0
            if middle[i][j] == upper[i][j]:
                Backtrack_m[i][j]= 1
            if middle[i][j] == middle[i-1][j-1] + f:
                Backtrack_m[i][j]= 2
    fout.write(str(middle[len(w)][len(v)])+'\n')
    print(middle)
    return(Backtrack_m)


def OUTPUTAligm(Backtrack, v, j, i):
    ans1 = ""
    ans2 = ""
    while(i != 0 or j != 0):
        if Backtrack[i][j] == 0:
            ans1 = ans1 + '-'
            ans2 = ans2 + str(w[i-1])
            i -= 1
        else:
            if Backtrack[i][j] == 1:
                ans1 = ans1 + str(v[j-1])
                ans2 = ans2 + str('-')
                j -= 1
            else:
                ans1 = ans1 + str(v[j-1])
                ans2 = ans2 + str(w[i-1])
                i -= 1
                j -= 1
    fout.write(ans1[::-1]+'\n')
    fout.write(ans2[::-1])

fin = open('input.txt', 'r')
fin2 = open('alp.txt', 'r')
fout=open('output.txt', 'w')
v=fin.readline().replace('\n','')
w=fin.readline().replace('\n','')
alp={}
a=fin2.readline().replace('  ',' ').replace('\n','').replace('  ','').split(' ')
i=0

for symb in a:
    alp[symb]=i
    i=i+1
score=[]
for line in fin2.readlines():
    s=line.replace('\n','').replace('  ',' ').split(' ')
    score.append([int(a) for a in s[1:]])
b=LCSBACKTRACK(v,w)
OUTPUTAligm(b,v,len(v),len(w))