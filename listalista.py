import random
tarolo = []
for i in range(4):
    sor = []
    for i in range(3):
        szam= random.randint(0,25)
        sor.append(szam)
    tarolo.append(sor)
print(tarolo)