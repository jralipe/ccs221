###Mandala Assignment using turtle.py for CCS 221 submitted by Carlo Antonio T. Taleon of BSCS-1A in WVSU-CICT (2020)
import turtle

###FUNCTION DECLARATIONS
def createClones(toclone, num_of_clones, angleModifier):
    '''Creates clones of a turtle and returns a list.'''
    turtle_list = []
    angle = 0
    for i in range(num_of_clones):
        turtle_list.append(toclone.clone())
        turtle_list[i].left(angle)
        angle += angleModifier

    return turtle_list

def curve(turtleObject,left_or_right,angle,speed, disableAnim):
    ''' Turns the turtle to a specific degree and speed.

        Parameters:
        >turtleObject: your turtleObject.
        >left_or_right: "left" to turn to the left and "right" to turn to the right.
        >degrees: at what degree the turtle stops after the curve. (e.g 180 for a U-turn.)
        >speed: recommended 1 or below.
    '''
    if disableAnim == True:
        turtle.tracer(False)
    if (left_or_right == "left"):
        for i in range(angle):
            turtleObject.left(1)
            turtleObject.forward(speed)
    elif (left_or_right == "right"):
        for i in range(angle):
            turtleObject.right(1)
            turtleObject.forward(speed)
    else:
        raise ValueError("Not a valid left or right value")

    turtle.tracer(True)

###turtle creation & window initalization
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(9999999999999999999999999999999999999999999999999999999999999)

###CLONING - Uses the createClones function to make 8 clones separated by 45 degrees from eachother.
t1 = createClones(t, 8, 45)
t.ht()

###DRAWING###

#LEAVES PATTERN
for turtles in t1:
    for i in range(10):
        turtles.pencolor("lightgreen"); turtles.pensize(2)
        turtles.color("lightgreen")
        turtles.forward(180*2)
        turtles.left(90)
        turtles.forward(50)
        turtles.left(60)
        turtles.left(20)

for turtles in t1:
    turtles.right(1700)
    turtles.setpos(0,0)
    turtles.pensize(1)

#WHITE PETAL PATTERN
for turtles in t1:
    turtles.pencolor("white"); turtles.fillcolor("white")
    turtles.begin_fill()
    turtles.forward(15)
    curve(turtles,"left", 45, 4, True)
    curve(turtles,"left", 45, 3.5, True)
    turtles.setposition(0,0)
    turtles.up()
    turtles.down()
    turtles.forward(15)
    curve(turtles,"right", 45, 4, True)
    curve(turtles,"right", 45, 3.5, True)
    turtles.end_fill()
    turtles.up()

#GOLD WEB-LIKE & SURROUNDING CIRCLES PATTERN
for turtles in t1:
    turtles.up()
    turtles.setposition(0,0)
    turtles.forward(180)
    turtles.left(180)
    turtles.down()
    turtles.begin_fill()
    turtles.pencolor("gold");turtles.color("gold"); turtles.pensize(2)
    curve(turtles, "left", 90+45, 1.3, True)
    turtles.setposition(0,0)
    turtles.right(90+45)
    turtles.end_fill()
    turtles.right(90+45)

    for i in range(3):
        turtles.pencolor("gold"); turtles.fillcolor("gold")
        turtles.up()
        turtles.setpos(0,0)
        turtles.forward(210)
        turtles.down()
        turtles.begin_fill()
        turtles.circle(15)
        turtles.end_fill()
        turtles.left(15)

#ORANGE INNER PETAL PATTERN
for turtles in t1:
    turtles.right(150.0+22.5)
    turtles.pencolor("orange"); turtles.fillcolor("orange")
    turtles.up()
    turtles.setposition(0,0)
    turtles.begin_fill()
    turtles.down()
    curve(turtles,"left", 90, 2.4, True)
    turtles.setposition(0,0)
    turtles.end_fill()

#RED INNER PETAL PATTERN
for turtles in t1:
    turtles.left(22.5)
    turtles.pencolor("red"); turtles.fillcolor("red")
    turtles.up()
    turtles.setposition(0,0)
    turtles.begin_fill()
    turtles.down()
    curve(turtles,"left", 90, 1.6, True)
    turtles.setposition(0,0)
    turtles.end_fill()

#WHITE INNER PETAL PATTERN
for turtles in t1:
    turtles.right(22.5)
    turtles.pencolor("white"); turtles.fillcolor("white")
    turtles.up()
    turtles.setposition(0,0)
    turtles.begin_fill()
    turtles.down()
    curve(turtles,"left", 90, 1, True)
    turtles.setposition(0,0)
    turtles.end_fill()

#CENTER-MOST GOLD CIRCLES PATTERN
for turtles in t1:
    turtles.up()
    turtles.pencolor("gold"); turtles.fillcolor("gold")
    turtles.forward(6)
    turtles.begin_fill()
    turtles.down()
    turtles.circle(1)
    turtles.end_fill()
    turtles.ht()

turtle.done()
