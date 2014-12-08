def LCSBACKTRACK(v, w):
    global  max_i
    global  max_j
    sc=0
    sigma=5
    global  score
    m=len(v)+1
    n=len(w)+1
    Backtrack=[[0 for x in range(m)]for y in range(n)]
    s=[[0 for x in range(m)]for y in range(n)]
    for i in range(n):
        s[i][0]= 0
        Backtrack[i][0] = 0
    for j in range(m):
        s[0][j] = 0
        Backtrack[0][j] = 1
    for i in range(1,len(w) + 1):
        for j in range(1,len(v) + 1):
            f=score[alp[v[j-1]]][alp[w[i-1]]]
            s[i][j] = max(0,s[i-1][j]-sigma, s[i][j-1]-sigma, s[i-1][j-1] + f)
            if s[i][j] == s[i-1][j]-sigma:
                Backtrack[i][j] = 0
            if s[i][j] == s[i][j-1]-sigma:
                Backtrack[i][j] = 1
            if s[i][j] == s[i-1][j-1] + f:
                Backtrack[i][j]= 2
            if s[i][j]==0:
                Backtrack[i][j]=-1
    maxS=0
    for i in range(len(w) + 1):
        for j in range(len(v) + 1):
            if(s[i][j]>maxS):
                max_i=i
                max_j=j
                maxS=s[i][j]
    fout.write(str(maxS)+'\n')
    return(Backtrack)

def OUTPUTAligm(Backtrack, v, j, i):
    ans1 = ""
    ans2 = ""
    while(i != 0 or j != 0):
        if Backtrack[i][j]==-1:
            break
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
max_i=0
max_j=0
b=LCSBACKTRACK(v,w)

OUTPUTAligm(b,v,max_j,max_i)