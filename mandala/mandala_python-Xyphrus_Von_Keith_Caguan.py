# Mandala Pattern
import turtle


x = turtle.Turtle()
win = turtle.Screen()
win.bgcolor("black")
x.color("white")
x.pensize(10)
x.speed(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

x.penup()
x.goto(50,155)
x.pendown()

for i in range(31):
    for i in range(8):
        x.forward(100)
        x.left(90)

    x.penup()
    x.right(35)
    x.forward(100)
    x.pendown()

x.penup()
x.goto(0,0)
x.pendown()

x.right(20)
for i in range(70):
    x.left(1)
    x.forward(2)

x.left(110)
for i in range(70):
    x.left(1)
    x.forward(2)

x.right(10)
for i in range(70):
    x.right(1)
    x.forward(2)

x.right(110)
for i in range(70):
    x.right(1)
    x.forward(2)

x.left(90)
for i in range(70):
    x.left(1)
    x.forward(2)

x.left(110)
for i in range(70):
    x.left(1)
    x.forward(2)

x.left(2)
for i in range(70):
    x.right(1)
    x.forward(2)

x.right(110)
for i in range(70):
    x.right(1)
    x.forward(2)

turtle.done()