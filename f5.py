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
    for i in range(1):
    
        Eszti.forward(50)
        Eszti.left(90)
        Eszti.forward(60)
        Eszti.left(90)
        Eszti.forward(70)
        Eszti.left(90)
        Eszti.forward(80)
        Eszti.left(90)
        Eszti.forward(90)
        Eszti.left(90)
        Eszti.forward(100)
        Eszti.left(90)
        Eszti.forward(110)
        Eszti.left(90)
        Eszti.forward(120)
        Eszti.left(90)
        Eszti.forward(130)
        Eszti.left(90)
        Eszti.forward(140)
        Eszti.left(90)
        Eszti.forward(150)
        Eszti.left(90)
        Eszti.forward(160)
        Eszti.left(90)
        Eszti.forward(170)
        Eszti.left(90)
        Eszti.forward(180)
        Eszti.left(90)
        Eszti.forward(190)
        Eszti.left(90)
        Eszti.forward(200)
        Eszti.left(90)
        Eszti.forward(210)
        Eszti.left(90)
        Eszti.forward(220)
        Eszti.left(90)
        Eszti.forward(230)
        Eszti.left(90)
        Eszti.forward(240)
        Eszti.left(90)
        Eszti.forward(250)
        Eszti.left(90)
        Eszti.forward(260)
        Eszti.left(90)
        Eszti.forward(270)
        Eszti.left(90)
        Eszti.forward(280)
        Eszti.left(90)
        Eszti.forward(290)
        Eszti.left(90)
        Eszti.forward(300)
        Eszti.left(90)
        Eszti.forward(310)
        Eszti.left(90)
        Eszti.forward(320)
        Eszti.left(90)
for i in range(1):
    negyzet(20)








a.mainloop()