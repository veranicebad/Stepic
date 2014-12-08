__author__ = 'Vera'
fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
table = open('integer_mass_table.txt', 'r')
mass={}
acid=[]
for line in table.readlines():
    t=line.split(' ')
    mass[t[0]]=int(t[1].replace('\n',''))
print acid,mass
p=fin.readline().replace("\n",'')
li=[]
fm=0
for j in range(len(p)):
    fm+=mass[p[j]]
    m=0
    for i in range(len(p)-1):
        li.append(m+mass[p[(j+i)%len(p)]])
        m+=mass[p[(j+i)%len(p)]]
li.append(0)
li.append(fm)
li.sort()
print li
for i in range(len(li)):
    fout.write(str(li[i])+' ')
fin.close()
fout.close()