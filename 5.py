import operator
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
s1=fin.readline().split(' ')
ans=[]
k=int(s1[0])
l=int(s1[1])
t=int(s1[2])
fout.write(str(s))
ans=[]
for i in range(len(s)-l):
    window=s[i:i+l]
    d={}
    for j in range(len(window)):
        if window[j:j+k] in d:
            d[window[j:j+k]]=d[window[j:j+k]]+1
        else:
            d[window[j:j+k]]=1
    #print d
    for key, value in d.items():
        if value>=t:
            if not(key in ans):
                ans.append(key)
                print key
                #fout.write(str(key)+' ')
fout.write(str(len(ans)))
fin.close()
fout.close()
