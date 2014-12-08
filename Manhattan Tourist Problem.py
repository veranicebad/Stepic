from plistlib import Data

def MANHATTANTOURIST(n, m, Down, Right):
    s=[[0 for x in range(m+1)]for y in range(n+1)]
    for i in range(1,n):
        s[i][0] = s[i-1][0] + Down[i-1][0]
    for j in range(1,m):
        s[0][j] = s[0][j-1]+ Right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i - 1][j] + Down[i-1][j], s[i][j - 1] + Right[i][j-1])
    print(s)
    return s[n][m]

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','').split(' ')
n=int(s[0])
m=int(s[1])
Down=[[0 for x in range(m+1)]for y in range(n)]
Right=[[0 for x in range(m)]for y in range(n+1)]
for i in range(n):
    s=fin.readline().replace('\n','').split(' ')
    for j in range(m+1):
        Down[i][j]=int(s[j])
fin.readline()
for i in range(n+1):
    s=fin.readline().replace('\n','').split(' ')
    for j in range(m):
        Right[i][j]=int(s[j])
print(MANHATTANTOURIST(n,m,Down,Right))
