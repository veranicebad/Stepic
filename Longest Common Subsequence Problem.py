def LCSBACKTRACK(v, w):
    print(v,w)
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
            if v[j-1] == w[i-1]:
                f=1
            else:
                f=0
            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + f)
            if s[i][j] == s[i-1][j]:
                Backtrack[i][j] = 0
            if s[i][j] == s[i][j-1]:
                Backtrack[i][j] = 1
            if s[i][j] == s[i-1][j-1] + 1 and f == 1:
                Backtrack[i][j]= 2
    return(Backtrack)

def OUTPUTLCS(Backtrack, v, j, i):
    ans = ""
    while(i != 0 or j != 0):
        if Backtrack[i][j] == 0:
            i -= 1
        else:
            if Backtrack[i][j] == 1:
                j -= 1
            else:
                ans = ans + str(v[j-1])
                i -= 1
                j -= 1
    fout.write(ans[::-1])

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
v=fin.readline().replace('\n','')
w=fin.readline().replace('\n','')
b=LCSBACKTRACK(v,w)
OUTPUTLCS(b,v,len(v),len(w))