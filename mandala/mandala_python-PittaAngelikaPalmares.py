import turtle
window = turtle.Screen()
window.bgcolor("#3B4255")
a = turtle.Turtle()
a.penup()
a.setposition(-90,-150)
a.color("#66C3B1")
a.shape("turtle")
a.width(5)
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
a.color("RED")
for i in range(14):
    for i in range(2):
        a.forward(140)
        a.right(110)
        a.forward(140)
        a.left(210)
a.up()
a.forward(90)
a.right(19)
a.forward(66)
a.down()
a.color("BLACK")
for i in range(14):
    for i in range(2):
        a.right(90)
        a.forward(44)
        a.left(40)


