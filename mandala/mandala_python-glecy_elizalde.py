import turtle

m = turtle.Turtle()
m.hideturtle()
m.width(2)
m.color("#000000")
m.fillcolor("#ffffff")
m.speed(0)

def circle(r):
    m.up()
    m.setpos(0,0)
    m.down()
    m.up()
    m.forward(r)
    m.down()
    m.left(90)
    m.circle(r)
    
def balls(a,b,c,d):
    for x in range(a):
            m.up()
            m.setpos(0,0)
            m.forward(b)
            m.down()
            m.left(90)
            m.circle(c)
            m.right(d)

def stmp(a, b, c):
    for x in range(a):
            m.up()
            m.setpos(0,0)
            m.forward(b)
            m.down()
            m.stamp()
            m.left(c)

def dot(a, b, c, d):
    for x in range(a):
            m.up()
            m.setpos(0,0)
            m.forward(b)
            m.down()
            m.left(90)
            m.dot(c)
            m.right(d)

def line(a, b, c, d):
    for x in range(a):
            m.up()
            m.setpos(0,0)
            m.forward(b)
            m.down()
            m.forward(c)
            m.right(d)
	
    
balls(8, 10, 40, 45)
dot(8, 45, 6, 45)

m.width(1)
balls(20, 80, 5, 72)

m.left(9)
balls(20, 89, 8, 72)
m.right(9)
stmp(20, 89, 18)

m.width(2)
circle(90)
circle(95)

m.width(1)
balls(20, 105, 5, 72)
m.left(9)
dot(20,100, 5, 72)

m.width(2)
circle(106)
line(40, 106, 6, 9)
circle(114)

m.left(4.5)
dot(40, 109, 4, 81)
m.right(4.5)

