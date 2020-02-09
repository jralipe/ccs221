import turtle
s = turtle.Turtle()
s.speed(10000)

for i in range (40):
        s.color("#9FB6CD")
        s.pensize(2)
        s.left(12)
        s.forward(200)
        s.left(90)
        s.forward(200)
        s.left(90)
        s.forward(200)
        s.left(90)
        s.forward(200)
        s.left(90)
        
      
def Circle(color,size):
    s.begin_fill()
    s.color(color)
    s.up()
    s.setposition(180,100)
    s.down()
    s.circle(size)
    s.end_fill()
    
Circle("#74BBFB",210)
s.color("white")

s.up()
s.setposition(0,0)
s.down()


def drawPattern (color,sides,size,iteration):
    s.color(color)
    for i in range (0,iteration):
        for j in range (0,sides):
            s.forward(size)
            s.left (360 / sides)
        s.left (360 / iteration)

s.pensize(2)
drawPattern ("#FFDEAD", 6, 80, 20)
s.hideturtle()
