align=[]

def OutPath(List):
    ans1=''
    ans2=''
    for i in range (List[0][0]):
        ans1=ans1+w[i]
        ans2=ans2+'-'
    if List[0][2] == 2:
            ans1=ans1+w[List[0][0]]
            ans2=ans2+v[List[0][1]]
    else:
            ans2=ans2+v[List[0][1]]
            ans1=ans1+'-'

    for i in range(1, len(List)):
        if List[i-1][0] + 1!=List[i][0]:
            for j in range(List[i-1][0] + 1, List[i][0]):
                    ans1=ans1+w[j]
                    ans2=ans2+'-'
        if List[i][2]==2:
            ans1=ans1+w[List[i][0]]
            ans2=ans2+v[List[i][1]]
        if List[i][2]==1:
            ans2=ans2+v[List[i][1]]
            ans1=ans1+'-'
        if List[i][2]==0:
            ans1=ans1+w[List[i][0]]
            ans2=ans2+'-'
    for i in range (List[-1][0] + 1, len(w)):
        ans1=ans1+w[i]
        ans2=ans2+'-'
    sc = 0
    for i in range(len(ans1)):
        if ans1[i] == '-' or ans2[i] == '-':
            sc -= sigma
        else:
            sc += score[alp[ans1[i]]][alp[ans2[i]]]
    print(sc)
    print(ans2)
    print(ans1)


def LINEARSPACEALIGNMENT(top, bottom, left, right):
    global  align
    if left == right:
        return
    if top == bottom:
        for i in range(left,right):
            align.append([top, i ,1, top])
        return
    middle = (left + right)/2
    #midNode = MiddleNode(top, bottom, left, right)
    midEdge = MiddleEdge(top, bottom, left, right)
    print(middle, midEdge[0], midEdge[2])
    LINEARSPACEALIGNMENT(top, midEdge[0], left, middle)

    align.append(midEdge[:])
    print(midEdge)
    if midEdge[2] == 1 or midEdge[2] == 2:
        middle = middle + 1
    if midEdge[2] == 0 or midEdge[2] == 2:
        midEdge[0] = midEdge[0] + 1

    LINEARSPACEALIGNMENT(midEdge[0], bottom, middle, right)
    print(midEdge)


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
    if len(v) == 0:
        return(s_prev)
    return(s)

def MiddleEdge(top, bottom, left, right):
    global v
    global w
    midle=(right-left+2)/2
    real_middle = left + midle
    x1=0
    y1=real_middle-1
    x2=0
    y2=real_middle
    w1=w[::]
    w1=w1[top:bottom]
    w2=w[::]
    w2=w2[top:bottom]
    v1=v[::]
    v1=v1[left:right]
    v2=v[::]
    v2=v2[left:right]
    w2=w2[::-1]
    v1=v1[:midle - 1]
    #print(v1)
    v2=v2[midle:][::-1]
    s1=Ss(v1,w1)
    s2=Ss(v2,w2)
    #print(v2,w2)
    #print(s1,s2)
    s2=s2[::-1]
    s_max=s1[0]+s2[0]-sigma
    for i in range(1,len(w1)+1):
        if s_max<s1[i]+s2[i]-sigma:
            s_max=s1[i]+s2[i]-sigma
            x1=i
            x2=i

        f=score[alp[v[real_middle-1]]][alp[w1[i-1]]]
        if s_max<s1[i-1]+s2[i]+f:
            s_max=s1[i-1]+s2[i]+f
            x1=i-1
            x2=i
    #print(x1,y1,x2,y2)
    if x1==x2:
        return([top + x1, y1, 1, top + x2])
    if x1<x2 and y1<y2:
        return([top + x1, y1, 2, top + x2])
    if y1==y2:
        return(0)

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
    st=line.replace('\n','').replace('  ',' ').split(' ')
    score.append([int(a) for a in st[1:]])
sigma = 5
n=len(v)
m=len(w)
LINEARSPACEALIGNMENT(0,len(w),0,len(v))
print(align)
OutPath(align)