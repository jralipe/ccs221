import turtle
window = turtle.Screen()
window.bgcolor("black")
a = turtle.Turtle()
a.setposition(-120,-150)
a.color("pink")
a.shape("turtle")
a.width(2)
a.penup()
a.back(220)
a.left(60)
a.speed(30)
a.pendown()
for i in range(20):
     for i in range(2):
        a.forward(300)
        a.right(60)
        a.forward(300)
        a.left(130)
        a.forward(300)
        a.left(180)
a.penup()
a.left(-28)
a.forward(236)
a.pendown()
a.width(0)
a.color("cyan","violet")
for i in range(20):
    for i in range(2):
        a.forward(110)
        a.right(40)
        a.forward(110)
        a.left(210)



