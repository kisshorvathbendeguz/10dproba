import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.shape("turtle")
Sanyi.speed(0)

szinek = ["yellow", "red", "purple", "blue"] 
for sz in szinek: 
    Sanyi.color(sz) 
    Sanyi.forward(50) 
    Sanyi.left(90)
    
Sanyi.penup()
Sanyi.forward(5)
Sanyi.left(90)
Sanyi.pendown()

for sz in szinek: 
    Sanyi.color(sz) 
    Sanyi.forward(50) 
    Sanyi.left(90)    
Sanyi.penup()
Sanyi.forward(5)
Sanyi.left(90)
Sanyi.pendown()

for sz in szinek: 
    Sanyi.color(sz) 
    Sanyi.forward(50) 
    Sanyi.left(90)    
Sanyi.penup()
Sanyi.forward(5)
Sanyi.left(90)
Sanyi.pendown()

for sz in szinek: 
    Sanyi.color(sz) 
    Sanyi.forward(50) 
    Sanyi.left(90)    
Sanyi.penup()
Sanyi.forward(5)
Sanyi.left(90)
Sanyi.pendown()

ablak.mainloop()