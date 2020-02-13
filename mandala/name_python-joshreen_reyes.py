import turtle

josh = turtle.Screen()
josh.bgcolor("black")

name = turtle.Turtle()
name.shape("turtle")
name.color("light blue")
name.width(5)

#Position
name.up()
name.setposition(-100,20)

#J
name.down()
name.forward(20)
name.left(180)
name.forward(40)
name.left(180)
name.forward(20)
name.right(90)
name.forward(30)
for i in range(180):
        name.right(1)
        name.forward(0.3)
#J
name.up()
name.right(180)
name.forward(17)
name.left(90)
name.forward(40+40)

#O
name.down()
name.circle(20)

#S
name.up()
name.forward(40)
name.down()
name.forward(9)
for i in range(180):
        name.left(1)
        name.forward(0.2)
for i in range(180):
        name.right(1)
        name.forward(0.2)
turtle.forward(5)

#H
name.up()
name.forward(25)
name.left(90)
name.down()
name.backward(50)
name.up()
name.forward(17)
name.down()
for i in range(180):
        name.right(1)
        name.forward(0.2)
name.forward(17)

turtle.done()


