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
def sokszog(sz):
    for i in range(4):
        Eszti.forward(sz)
        Eszti.left(45)
        Eszti.forward(50)
        Eszti.left(45)

for i in range(1):
    sokszog(50)
a.mainloop()