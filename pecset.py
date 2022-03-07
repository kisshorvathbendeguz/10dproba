import turtle 
ablak = turtle.Screen() 
ablak.bgcolor("lightgreen") 
Eszti = turtle.Turtle() 
Eszti.shape("turtle") 
Eszti.color("blue")

Eszti.penup()  #Ez új 9 
meret = 20  
for i in range(30): 
    Eszti.stamp()  #Hagyj egy lenyomatot a vásznon! 12 
    meret = meret + 3 #Növeld a méretet minden ismétlésnél! 
    Eszti.forward(meret)  #Mozgasd ... 14 
    Eszti.right(24) # ... és fordítsd Esztit!

ablak.mainloop()
