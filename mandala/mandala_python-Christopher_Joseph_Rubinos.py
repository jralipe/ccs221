import turtle

def back (mandala):
    mandala.shape("square")
    mandala.turtlesize(21)
    mandala.stamp()
    mandala.right(45)
    mandala.stamp()

def circle (mandala):
    mandala.up()
    mandala.sety(-210)
    mandala.down()
    mandala.begin_fill()
    mandala.circle(210)
    mandala.end_fill()
    mandala.hideturtle()


def home (mandala):
    mandala.showturtle()
    mandala.up()
    mandala.home()
    mandala.down()


def pink (mandala):
    for i in range(8):
        mandala.right(45*i)
        for x in range(30):
            mandala.down()
            mandala.stamp()
            mandala.forward(10)
            mandala.stamp()
            mandala.up()
        mandala.right(135)
        for y in range(42):
            mandala.down()
            mandala.stamp()
            mandala.forward(10)
            mandala.stamp()
            mandala.up()
        mandala.home()
    mandala.down()


def purple (mandala):
    clones = []
    angle = 60
    
    for i in range(12):
        clones.append(mandala.clone())
        clones[i].left(angle)
        angle = angle + (360/12)

    for clone in clones:
        clone.begin_fill()
        clone.forward(208)
        clone.left(160)
        clone.forward(120)
        clone.end_fill()
        clone.hideturtle()


def lavender (mandala):
    clones = []
    angle = 0
    
    for i in range(12):
        clones.append(mandala.clone())
        clones[i].right(angle)
        angle = angle + (360/12)

    for clone in clones:
        clone.begin_fill()
        clone.forward(208)
        clone.right(170)
        clone.forward(140)
        clone.end_fill()
        clone.hideturtle()


def white (mandala):
    clones = []
    angle = 90

    for i in range(6):
        clones.append(mandala.clone())
        clones[i].left(angle)
        angle = angle + (360/6)
    
    for clone in clones:
        clone.begin_fill()
        clone.forward(150)
        clone.right(160)
        clone.forward(110)
        clone.end_fill()
        clone.hideturtle() 


def salmon (mandala):
    clones = []
    angle = 90

    for i in range(6):
        clones.append(mandala.clone())
        clones[i].left(angle)
        angle = angle + (360/6)
    
    for clone in clones:
        clone.begin_fill()
        clone.forward(150)
        clone.left(160)
        clone.forward(97)
        clone.end_fill()
        clone.hideturtle()    

##############################################################
mandala = turtle.Turtle()

mandala.shape("circle")
mandala.pensize(3)
mandala.turtlesize(.5)
mandala.speed(11)

screen = turtle.getscreen()
screen.bgcolor("black")

mandala.color("spring green")
back(mandala) #
home(mandala)

mandala.turtlesize(.5)
mandala.shape("circle")

mandala.color("aqua")
circle(mandala) #
home(mandala) #


mandala.color("magenta")
pink(mandala) #


mandala.pensize(5)
mandala.color("lavender", "orchid")
purple(mandala) #

mandala.color("lavender")
lavender(mandala) #


mandala.pensize(5)
mandala.color("salmon", "light yellow")
white(mandala) #

mandala.color("salmon")
salmon(mandala) #

turtle.done()

'''
THE Carlo Taleon helped me with understanding the clones thing
https://docs.python.org/3/library/turtle.html
^^ used this website for other turtle stuff
https://trinket.io/docs/colors
^^ this for colors
'''
