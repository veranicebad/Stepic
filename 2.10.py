__author__ = 'Vera'

from copy import  deepcopy

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')

class Peptide:
     __slots__ = ['masslist', 'mass', 'cyclospectrum','score']
     def __init__(self):
         self.masslist=[0]
         self.mass=0
         self.cyclospectrum=[]
         self.score=0

def Expand(List):
    List_t=[]
    for peptide in List:
        for value in range(57,201):
            temp_peptide=deepcopy(peptide)
            temp_peptide.masslist.append(value)
            temp_peptide.mass+=value
            temp_peptide.cyclospectrum=Cyclospectrum(temp_peptide)
            temp_peptide.score=Score(temp_peptide.cyclospectrum,Spectrum)
            List_t.append(temp_peptide)
    if(len(List_t) >= 20000):
        List_t.sort(comparator)
    List_t = List_t[0:15000]
    return List_t

def Cyclospectrum(peptide):
    li=[]
    peptide_t=Peptide()
    peptide_t.masslist=peptide.masslist[1:]
    for j in range(len(peptide_t.masslist)):
        m=0
        for i in range(len(peptide_t.masslist)-1):
            li.append((m+peptide_t.masslist[(j+i)%len(peptide_t.masslist)]))
            m+=peptide_t.masslist[(j+i)%len(peptide_t.masslist)]
    li.append(0)
    li.append(peptide_t.mass)
    li.sort()
    return li

def spectrum(peptide):
    li=[]
    for j in range(1, len(peptide.masslist)):
        m=0
        for i in range(len(peptide.masslist)-j):
            li.append(m+peptide.masslist[(j+i)])
            m+=peptide.masslist[(j+i)]
    li.append(0)
    li.sort()
    return li

def Score(spectrum_peptide, Spectrum):
    Spectrum_t=Spectrum[:]
    score=0
    for p in spectrum_peptide:
        if p in Spectrum_t:
            Spectrum_t.remove(p)
            score=score+1
    return score

def comparator(p1,p2):
    return -p1.score+p2.score

def Cut(Leaderboard, Spectrum, N):
    ans=[]
    Leaderboard.sort(comparator)
    for i in range(min(N, len(Leaderboard))):
        ans.append(Leaderboard[i])
    for p in Leaderboard[N:]:
        if p.score == Leaderboard[N-1].score:
            ans.append(p)
        else:
            break
    return ans

def LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N):
    parentMass = max(Spectrum)
    Leaderboard=[]
    Leaderboard_tmp=[]
    peptide0 = Peptide()
    Leaderboard.append(peptide0)
    Leaderboard_tmp=Leaderboard[:]
    LeaderPeptide=peptide0
    Spectrum.sort()
    leaderScore = 0
    Leader_TEMP=[]
    while len(Leaderboard_tmp)!=0:
        Leaderboard = Expand(Leaderboard)
        Leaderboard_tmp=Leaderboard[:]
        for peptide in Leaderboard_tmp:
            if peptide.mass == parentMass:
                if peptide.score > leaderScore:
                    Leader_TEMP = []
                if peptide.score >= leaderScore:
                    LeaderPeptide = peptide
                    Leader_TEMP.append(LeaderPeptide)
                    leaderScore = LeaderPeptide.score
                    #print(LeaderPeptide,Score(Cyclospectrum(LeaderPeptide), Spectrum))
            elif peptide.mass > parentMass:
                Leaderboard.remove(peptide)
        Leaderboard = Cut(Leaderboard, Spectrum, N)
        print(len(Leaderboard))
        Leaderboard_tmp=Leaderboard[:]
    scorelp=[]
    print('Here!')
    for lp in Leader_TEMP:
        scorelp.append(lp.score)
    #print(Leader_TEMP)
    m = max(scorelp)
    print(m)
    for i in range(len(Leader_TEMP)):
        if scorelp[i]==m:
            leader=Leader_TEMP[i]
            print(leader.masslist[1:],leader.score,'!')
            fout.write("-".join(str(x) for x in leader.masslist[1:])+" ")
N=int(fin.readline())
Spectrum=[int(x) for x in (fin.readline().split(' '))]
LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum,N)
fin.close()
fout.close()