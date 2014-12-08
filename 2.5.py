__author__ = 'Vera'
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
table = open('integer_mass_table.txt', 'r')
mass={}
acid=[]
for line in table.readlines():
    t=line.split(' ')
    mass[t[0]]=int(t[1].replace('\n',''))
p=int(fin.readline())
count=[]
count.append(1)
for i in range(p+1):
    count.append(0)
    for value in mass.values():
        if i>=value:
           count[i]+=count[i-value]
print count[p]
fout.write(str(count[p]))

fin.close()
fout.close()