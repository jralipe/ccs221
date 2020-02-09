###4 Letters of Name Activity using turtle.py for CCS 221 submitted by Carlo Antonio T. Taleon of BSCS-1A in WVSU-CICT (2020)
import turtle

###FUNCTION DECLARATIONS
def curve(turtleObject,left_or_right,angle,speed, disableAnim):
    ''' Turn your turtle to a specific degree and speed

        Parameters:
        turtleObject: your turtleObject.
        left_or_right: "left" to turn to the left and "right" to turn to the right.
        degrees: at what degree the turtle stops after the curve. (e.g 180 for a U-turn.)
        speed: recommended 1 or below.
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

def drawC ():
    '''Draws a C and goes to the rightdownmost part of the letter and faces x+'''
    startPos = carlo.pos()
    carlo.up()
    carlo.right(90)
    carlo.backward((90/2)+10)
    carlo.down()
    curve(carlo,"right",90,1, True)
    carlo.forward(10)
    curve(carlo,"right",90,1, True)
    carlo.forward(100)
    curve(carlo,"right",90,1, True)
    carlo.forward(10)
    curve(carlo,"right",90,1, True)
    carlo.up()
    carlo.setpos(startPos)
    carlo.left(90)

def drawA ():
    '''Draws an A and goes to the rightdownmost part of the letter and faces x+'''
    carlo.up()
    carlo.down()
    carlo.left(90)
    carlo.forward(28+100+28)
    curve(carlo,"right",180,1, True)
    carlo.forward((156/2)-20)
    carlo.right(90)
    carlo.forward(110)
    carlo.backward(110)
    carlo.left(90)
    carlo.forward((156/2)+20)
    carlo.up()
    carlo.left(90)
    ##carlo.

def drawR ():
    '''Draws an R and goes to the rightdownmostpart of the letter and faces x+'''
    carlo.up()
    carlo.down()
    carlo.left(90)
    carlo.forward(28+156+28)
    carlo.right(90)
    carlo.forward(58)
    curve(carlo,"right",180,1,True)
    carlo.forward(55)
    carlo.backward(55)
    carlo.left(115)
    carlo.forward(105)
    carlo.up()
    carlo.left(65)

def drawL ():
    '''Draws an L and goes to the rightdownmostpart of the letter and faces x+'''
    carlo.up()
    carlo.down()
    carlo.left(90)
    carlo.forward(156+28+28)
    carlo.backward(156+28+28)
    carlo.right(90)
    carlo.forward(130)
    carlo.up()

###turtle creation & window initalization
carlo = turtle.Turtle(); carlo.color("black")
carlo.shape("arrow");carlo.shapesize(3)
carlo.pencolor("white");carlo.pensize(15)
carlo.up(); carlo.setpos(-180, 50) #sets starting position

turtle.bgcolor("red")

###Drawing
drawC()
turtle.bgcolor("orange") #colorchange
carlo.forward(50) #space between letter
drawA()
turtle.bgcolor("yellow") #colorchange
carlo.forward(50) #space between letter
drawR()
turtle.bgcolor("green") #colorchange
carlo.forward(50) #space between letter
drawL()
turtle.bgcolor("black") #colorchange
carlo.hideturtle()
turtle.done()





