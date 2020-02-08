# Activity in Visual Graphics

import turtle

x = turtle.Turtle()
x.color("blue")
x.pencolor("red")
x.pensize(50)

# Setting of starting position
x.penup()
x.goto(-500,0)
x.left(45)
x.forward(100)
x.pendown()

# Letter X
x.left(180)
x.forward(200)
x.penup()
x.left(180)
x.forward(100)
x.left(90)
x.forward(100)
x.pendown()
x.left(180)
x.forward(200)


# To Y
x.left(45)
x.penup()
x.forward(75)
x.left(45)
x.forward(200)
x.left(180)
x.pendown()

# Letter Y
x.forward(200)
x.penup()
x.left(180)
x.forward(100)
x.left(90)
x.forward(100)
x.left(180)
x.pendown()
x.forward(100)

# Transition
x.penup()
x.forward(100)
x.left(45)
x.forward(75)
x.left(90)
x.forward(150)
x.pendown()

# Letter P
x.left(180)
x.forward(150)
x.penup()
x.left(180)
x.forward(150)
x.pendown()
x.right(90)
x.forward(30)

i = 0
while i < 14:
    x.right(12)
    x.forward(10)
    i = i + 1
x.right(10)
x.forward(30)

# Transition to H
x.penup()
x.left(88)
x.forward(50)
x.left(90)
x.forward(150)
x.pendown()

# Letter H
x.penup()
x.left(90)
x.forward(150)
x.left(180)
x.pendown()
x.forward(150)
x.penup()
x.left(180)
x.forward(75)
x.right(90)
x.pendown()
x.forward(75)
x.penup()
x.left(90)
x.forward(75)
x.left(180)
x.pendown()
x.forward(150)

# Transition
x.penup()
x.left(90)
x.forward(80)
x.left(90)
x.forward(150)
x.left(180)
x.pendown()

# Letter R
x.pendown()
x.forward(150)
x.penup()
x.left(180)
x.forward(150)
x.pendown()
x.right(90)
x.forward(30)

i = 0
while i < 12:
    x.right(12)
    x.forward(10)
    i = i + 1
x.right(35)
x.forward(30)
x.penup()
x.left(180)
x.forward(30)
x.pendown()
x.right(65)
x.forward(65)

# Transition
x.penup()
x.left(65)
x.forward(80)
x.left(90)
x.forward(150)
x.left(180)
x.pendown()

# Letter U
x.forward(105)
i = 0
while i < 14:
    x.left(12)
    x.forward(10)
    i = i + 1
x.left(10)
x.forward(105)

# Transition
x.penup()
x.right(90)
x.forward(120)
x.left(180)
x.pendown()

# Letter S
x.forward(30)
i = 0
while i < 10:
    x.left(18)
    x.forward(11)
    i = i + 1
x.left(10)

i = 0
while i < 11:
    x.right(18)
    x.forward(12)
    i = i + 1
x.right(5)
x.forward(20)

turtle.done()
