import turtle

window=turtle.Screen()
window.bgcolor('black')
j=turtle.Turtle()

j.width(10)
j.shape('turtle')

#letter J
j.color('pink')
j.up()
j.setpos(-300, 0)
j.down()
j.forward(100)
j.left(180)
j.forward(50)
j.left(90)
j.forward(100)

def curveright (turtol, end_degree, speed):
    turtle.tracer(False)
    for i in range(end_degree):
        turtol.right(1)
        turtol.forward(speed)
    turtle.tracer(True)

curveright(j, 180, 0.5)
 
#letter I
j.up()
j.right(180)
j.forward(30)
j.left(90)
j.forward(160)
j.down()
j.left(90)
j.forward(125)
j.right(90)
j.right(90)
j.forward(125)
j.left(90)

#letter R
j.up()
j.forward(60)
j.left(90)
j.down()
j.forward(125)
j.right(90)
j.forward(20)
curveright (j, 180, 0.6)
j.forward(20)
j.left(180)
j.forward(30)
j.right(65)
j.forward(64)
j.left(65)

#letter A
j.up()
j.forward(55)
j.left(70)
j.down()
j.forward(130)
j.right(70)
j.right(70)
j.forward(130)
j.backward(55)
j.right(110)
j.forward(48)
j.backward(48)
j.left(110)
j.forward(55)
j.left(70)

j.up()
j.forward(60)
j.left(90)
j.down()
j.forward(125)
j.backward(125/2)
j.right(90)
j.forward(80)
j.right(90)
j.backward(125/2)
j.forward(125)
