__author__ = 'Vera'
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
Spectrum=[int(x) for x in (fin.readline().split(' '))]
print(Spectrum)
conv=[]
for i in range(len(Spectrum)):
    for j in range(i+1,len(Spectrum)):
        if i!=j:
            c=abs(Spectrum[i]-Spectrum[j])
            if c!=0:
                conv.append(c)
for c in conv:
    fout.write(str(c)+' ')