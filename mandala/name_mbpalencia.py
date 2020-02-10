import turtle
yam = turtle.Turtle()
window = turtle.Screen()

yam.color("white")
yam.goto(-300,-100)
yam.clear()
#M
yam.color("yellow")
yam.shape("triangle")
yam.pensize(10)
yam.setheading(90)
yam.forward(180)
yam.setheading(-60)
yam.forward(100)
yam.setheading(70)
yam.forward(95)
yam.setheading(-80)
yam.forward(195)

#A
yam.color("white")
yam.goto(-150,-100)

yam.color("yellow")
yam.shape("triangle")
yam.pensize(10)
yam.left(200)
yam.setheading(75)
yam.forward(180)
yam.setheading(-75)
yam.forward(180)
yam.backward(90)
yam.right(100)
yam.forward(50)
yam.backward(60)

#Y
yam.color("white")
yam.goto(-20,-80)

yam.color("yellow")
yam.shape("triangle")
yam.left(200)
yam.setheading(50)
yam.forward(145)
yam.backward(60)
yam.right(270)
yam.forward(80)


#B
yam.color("white")
yam.goto(110,90)

yam.color("yellow")
yam.shape("triangle")
yam.left(130)
yam.forward(200)
yam.backward(190)
yam.right(50)
yam.circle(50,-200)
yam.forward(10)
yam.right(-120)
yam.circle(60,-150)

turtle.done()
