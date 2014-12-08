def TOPOLOGICALORDERING(Candidates, out, incom):
    List=[]
    while not(len(Candidates)==0):
        c=Candidates[0]
        List.append(c)
        if not(c in out.keys()):
            Candidates.remove(c)
        else:
            Candidates.remove(c)
            for b in out[c]:
                #out[c].remove(b)

                incom[b].remove(c)
                if len(incom[b])==0:
                    Candidates.append(b)
            out[c]=[]
    #print(List)
    incomming=0
    outcomming=0
    print(incom, out)
    for i in incom.keys():
        incomming=incomming+len(incom[i])
    for i in out.keys():
        outcomming=outcomming+len(out[i])
    if (incomming!=0)or(outcomming!=0):
        return "the input graph is not a DAG"
    else:
        return List

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
out={}
incom={}
for line in fin.readlines():
    s=line.replace('\n','').split(' ')
    i=int(s[0])
    ou=[int(o) for o in s[2].split(',')]
    for o in ou:
        if i in out.keys():
            out[i].append(o)
        else:
            out[i]=[]
            out[i].append(o)
        if o in incom.keys():
            incom[o].append(i)
        else:
            incom[o]=[]
            incom[o].append(i)
m=max(out.keys())
Candidates=[]
for i in range(m+1):
    if not(i in incom.keys()):
        Candidates.append(i)
print(Candidates)
print(out)
print(incom)
l=TOPOLOGICALORDERING(Candidates,out,incom)
if l=="the input graph is not a DAG":
    fout.write(l)
else:
    fout.write(', '.join([str(a) for a in l]))