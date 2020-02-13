import turtle

window = turtle.Screen()
window.bgcolor("#333333")
c = turtle.Turtle()
c.shape("circle")
c.color("medium purple")
c.pensize(9)
c.speed(3)

h = c.clone()
r = c.clone()
i = c.clone()


def LetterC (c):
    c.backward(75)
    c.left(90)
    c.forward(100)
    c.right(90)
    c.forward(75)
    c.hideturtle()

def LetterH (h):
    h.up()
    h.forward(25)
    h.down()
    h.left(90)
    h.forward(100)
    h.backward(50)
    h.right(90)
    h.forward(50)
    h.right(90)
    h.forward(50)
    h.hideturtle()
    
def LetterR (r):
    r.up()
    r.forward(100)
    r.down()
    r.left(90)
    r.forward(75)
    r.backward(20)
    r.right(90)
    r.forward(40)
    r.right(90)
    r.forward(25)
    r.hideturtle()
    

def LetterI (i):
    i.up()
    i.forward(160)
    i.down()
    i.left(90)
    i.forward(50)
    i.up()
    i.forward(20)
    i.down()
    i.turtlesize(.7)
    i.stamp()
    turtle.done()

LetterC(c)
LetterH(h)
LetterR(r)
LetterI(i)

