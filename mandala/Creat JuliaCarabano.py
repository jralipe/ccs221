import turtle

window=turtle.Screen()
window.bgcolor("#060000")
jul=turtle.Turtle()
jul.pencolor("#008083")
jul.pensize(10)
jul.up()
jul.setposition(-140,50)

#Border
for i in range(2):
    jul.down()
    jul.forward(330)
    jul.right(90)
    jul.forward(150)
    jul.right(90)
    jul.up()
    jul.forward(50)
    jul.down()
#J
jul.up()
jul.right(90)
jul.forward(35)
jul.left(90)
jul.down()
jul.forward(60)
jul.left(180)
jul.forward(30)
jul.left(180)
jul.right(90)
jul.forward(60)
turtle.tracer(False)
for i in range(180):
        jul.right(1)
        jul.forward(0.3)
turtle.tracer(True)
jul.up()
jul.right(90)
jul.forward(80)

#U
jul.down()
jul.left(90)
jul.forward(60)
jul.up()
jul.right(90)
jul.forward(35)
jul.down()
jul.right(90)
jul.forward(60)
turtle.tracer(False)
for i in range(180):
        jul.right(1)
        jul.forward(0.3)
turtle.tracer(True)     

#L
jul.up()
jul.right(90)
jul.forward(70)
jul.down()
jul.left(90)
jul.forward(60)
jul.left(180)
jul.forward(80)
jul.left(90)
jul.forward(35)

#I
jul.up()
jul.forward(30)
jul.left(90)
jul.down()
jul.forward(80)

#A
jul.up()
jul.right(90)
jul.forward(70)
jul.right(90)
jul.forward(20)
jul.down()
jul.forward(60)
jul.up()
jul.right(90)
jul.forward(35)
jul.down()
jul.right(90)
jul.forward(60)
turtle.tracer(False)
for i in range(200):
        jul.right(1)
        jul.forward(0.3)
turtle.tracer(True)
jul.right(70)
jul.forward(35)

turtle.done()