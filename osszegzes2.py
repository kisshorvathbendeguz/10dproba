szam = int(input('Adj meg egy számot -,05 és 5 között'))
összeg = 0
list =[]
while -5 <= szam >= 5:
    list.append(szam)
    összeg = összeg + szam
    szam = int(input('Adj meg egy számot -,05 és 5 között'))
print(list)
print("összeg:", összeg)