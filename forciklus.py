import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()

for sz in ["yellow", "red", "purple", "blue"]: 
    Sanyi.color(sz) 
    Sanyi.forward(50) 
    Sanyi.left(90)

ablak.mainloop()