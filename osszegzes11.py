import random
list =[]
összeg = 0
for i in range(5):
    szam = random.randint(1,10)
    list.append(szam)
    if szam % 2 == 0:
        összeg = összeg +szam
print('A lista elemei: ', list)
print('Az összeg: ', összeg)