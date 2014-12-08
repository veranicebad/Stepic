import copy

def TOPOLOGICALORDERING():
    global Candidates
    global out
    global incom
    global start
    #incom[start]=[]
    out_t=copy.deepcopy(out)
    incom_t=copy.deepcopy(incom)
    List=[]
    while not(len(Candidates)==0):
        c=Candidates[0]
        List.append(c)
        if not(c in out_t.keys()):
            Candidates.remove(c)
        else:
            Candidates.remove(c)
            for b in out_t[c]:
                incom_t[b].remove(c)
                if len(incom_t[b])==0:
                    Candidates.append(b)
            out_t[c]=[]
    incomming=0
    outcomming=0
    for i in incom_t.keys():
        incomming=incomming+len(incom_t[i])
    for i in out_t.keys():
        outcomming=outcomming+len(out_t[i])
    if (incomming!=0)or(outcomming!=0):
        return "the input graph is not a DAG"
    else:
        return List


def LCSBACKTRACK():
    global incom
    global m
    global start
    global n
    global List
    Backtrack=[0 for x in range(n+1)]
    s=[0 for y in range(n+1)]
    #Backtrack[0] = 0

    for b in List[1:]:
        max_s=-1
        if not(b in incom.keys()):
            s[b]=0
            Backtrack[b]=-1
            return
        for a in incom[b]:
            max_s=max(max_s,s[a]+m[a][b])
            s[b]=max_s
        for a in incom[b]:
            if max_s == s[a]+m[a][b]:
                Backtrack[b] = a
        print(b, max_s, Backtrack[b])
    return(Backtrack)

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
out={}
incom={}
start=int(fin.readline().replace('\n',''))
finish=int(fin.readline().replace('\n',''))
m=[[-1 for x in range(100)]for y in range(100)]
for line in fin.readlines():
    s=line.replace('\n','').split('->')
    i=int(s[0])
    s2=s[1].split(':')
    j=int(s2[0])
    w=int(s2[1])
    m[i][j]=w
    if i in out.keys():
        out[i].append(j)
    else:
        out[i]=[]
        out[i].append(j)
    if j in incom.keys():
        incom[j].append(i)
    else:
        incom[j]=[]
        incom[j].append(i)
n=max(out.keys())
n2=max(incom.keys())
n=max(n,n2)
Candidates=[]

for i in range(n+1):
    if not(i in incom.keys()) and i in out.keys():
        Candidates.append(i)
while(len(Candidates)!=1):
    lostCand = []
    newCand = []
    for c in Candidates:
        if(c!=start):
            for b in out[c]:
                incom[b].remove(c)
            out.pop(c)
            lostCand.append(c)
    for i in range(n+1):
        if i in incom.keys() and (incom[i]==[]):
            incom.pop(i)
        if not(i in incom.keys()) and i in out.keys():
            newCand.append(i)
    for i in lostCand:
        Candidates.remove(i)
    for i in newCand:
        if i not in Candidates:
            Candidates.append(i)

List=TOPOLOGICALORDERING()
print(List)
if List=="the input graph is not a DAG":
    fout.write(List)
else:
    Backtrack=LCSBACKTRACK()
    path=[]
    t=finish
    while(t!=start):
        print(t)
        path.append(t)
        t=Backtrack[t]
    path.append(t)
    ans=''
    for p in reversed(path):
        ans=ans+'->'+str(p)
    fout.write(ans[2:])
    print(ans[2:])