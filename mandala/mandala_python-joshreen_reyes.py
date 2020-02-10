import turtle

window = turtle.Screen()
window.bgcolor('white')

#Outer Flower
outer = turtle.Turtle()
outer.speed(0.5)
outer.width(2)
outer.color("green","yellow green")
outer.begin_fill()
for i in range(40):
    outer.circle(200,70)
    outer.left(110)
    outer.circle(200,70)
outer.end_fill()
outer.hideturtle()

#Middle Flower
middle = turtle.Turtle()
middle.speed(0.5)
middle.width(2)
middle.color("red","pink")
middle.begin_fill()
for i in range(8):
    middle.circle(90,135)
    middle.left(135)
    middle.right(90)
    middle.circle(90,135)
middle.end_fill()
middle.hideturtle()

#Inner Flower
inner = turtle.Turtle()
inner.speed(0.5)
inner.width(2)
inner.color("maroon","yellow")
inner.begin_fill()
for i in range(20):
    inner.circle(30,350)
    inner.right(135-15)
    inner.circle(30,350)
inner.end_fill()
inner.hideturtle()

#Dot
dot = turtle.Turtle()
dot.speed(0.5)
for i in range(8):
    dot.up()
    dot.setpos(0,0)
    dot.fd(124)
    dot.down()
    dot.dot(7)
    dot.left(45)
dot.hideturtle()

#Mini Circle
mc = turtle.Turtle()
mc.speed(0.5)
mc.color("red","white")
mc.begin_fill()
for i in range(8):
    mc.up()
    mc.setpos(0,0)
    mc.fd(110)
    mc.left(90)
    mc.down()
    mc.circle(7)
    mc.left(45)
mc.end_fill()

    
turtle.done()
