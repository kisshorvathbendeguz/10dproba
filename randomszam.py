import random 

random_szam = random.randint(1,3)

szam1 = int(input('Adj meg egy számot 1 és 3 között! '))
if szam1 == random_szam:
    print('A random generált szám ugyanaz mint a felhasználó által megadott szám.')
else:
    print('A random generált szám nem ugyanaz mint a felhasználó által megadott szám.')
print('>> A program vége! <<')



