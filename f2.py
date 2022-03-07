import turtle
def ablak_keszites(szin, ablaknev):

    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a


def teknoc_keszites(szin, tm):
    t = turtle.Turtle()
    t.color(szin)
    t.speed(0)
    t.pensize(tm)
    return t


a = ablak_keszites("lightgreen", "Eszti és Sanyi táncol")
Eszti = teknoc_keszites("hotpink", 5)
Sanyi = teknoc_keszites("black", 1)
David = teknoc_keszites("yellow", 2)
def negyzet(sz):
    for i in range(4):
        Eszti.forward(sz)
        Eszti.left(90)
    Eszti.penup()
    Eszti.right(90)
    Eszti.forward(10)
    Eszti.left(90)
    Eszti.backward(10)
    Eszti.pendown()

for i in range(1):
    negyzet(20)
for i in range(1):
    negyzet(40)
for i in range(1):
    negyzet(60)
for i in range(1):
    negyzet(80)
for i in range(1):
    negyzet(100)








a.mainloop()