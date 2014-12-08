__author__ = 'Vera'

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
table = open('integer_mass_table.txt', 'r')
mass={}
acid=[]
for line in table.readlines():
    t=line.split(' ')
    mass[t[0]]=int(t[1].replace('\n',''))

def Expand(List):
    List_t=[]
    for peptide in List:
        for value in mass.values():
            temp_peptide=peptide[:]
            temp_peptide.append(value)
            List_t.append(temp_peptide)
    return List_t

def Mass(peptide):
    mass=0
    for i in peptide:
        mass=mass+i
    return mass

def Cyclospectrum(Peptide):
    li=[]
    fm=0
    Peptide_t=Peptide[1:]
    for j in range(len(Peptide_t)):
        fm+=Peptide_t[j]
        m=0
        for i in range(len(Peptide_t)-1):
            li.append(str(m+Peptide_t[(j+i)%len(Peptide_t)]))
            m+=Peptide_t[(j+i)%len(Peptide_t)]
    li.append(str(0))
    li.append(str(fm))
    li.sort()
    return li

def spectrum(Peptide):
    li=[]
    for j in range(1, len(Peptide)):
        m=0
        for i in range(len(Peptide)-j):
            li.append(m+Peptide[(j+i)])
            m+=Peptide[(j+i)]
    li.append(0)
    li.sort()
    return li


def consistent(spectrum_peptide,Spectrum):
    Spectrum_t=Spectrum[:]
    for p in spectrum_peptide:
        if str(p) in Spectrum_t:
            Spectrum_t.remove(str(p))
        else:
            return False
    return True

def CYCLOPEPTIDESEQUENCING(Spectrum):
    List=[]
    List_tmp=[]
    peptide0=[]
    peptide0.append(0)
    List.append(peptide0)
    List_tmp=List[:]
    parentMass = Spectrum[-1]
    Spectrum.sort()
    while (len(List_tmp)!=0):
        List = Expand(List)
        List_tmp=List[:]
        #print(List)
        for peptide in List_tmp:
            if str(Mass(peptide)) == parentMass:
                if Cyclospectrum(peptide) == Spectrum:
                    for i in range(1,len(peptide)-1):
                        fout.write(str(peptide[i])+'-')
                    fout.write(str(peptide[len(peptide)-1]))
                    fout.write("\n")
                List.remove(peptide)
            elif not(consistent(spectrum(peptide), Spectrum)):
                List.remove(peptide)
        List_tmp=List[:]
Spectrum=(fin.readline().split(' '))
CYCLOPEPTIDESEQUENCING(Spectrum)
fin.close()
fout.close()