def DPCHANGE(money, Coins):
    MinNumCoins=[]
    MinNumCoins.append(0)
    for m  in  range(1,money+1):
        MinNumCoins.append(10000)
        for i in range(len(Coins)):
            if m >= Coins[i]:
                if MinNumCoins[m - Coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - Coins[i]] + 1
    print(MinNumCoins)
    return(MinNumCoins[money])

fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
money=int(fin.readline().replace('\n',''))
Coins=[]
Coins=[int(c) for c in fin.readline().replace('\n','').split(',')]

print(DPCHANGE(money, Coins))