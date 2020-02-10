'''MANDALA PATTERN by JIEZEL A. MAGLALANG of BSCS 1 - A'''

import turtle
from random import randint # CUSTOMIZED CODE FROM https://www.instructables.com/id/Easy-Designs-Turtle-Graphics-Python/

ji = turtle.Turtle()
turtle.bgcolor("black")
ji.shape("arrow")
ji.speed(9999999999999999999999999999999999999999999999999999999999999999999999999999*1000000000000000000000000000000000000000000000000000000000000000000000)
turtle.colormode(255)
r = randint(0,255)  # makes variables r,g,b whose value is an integer,
g = randint(0,255)  # which is between 0 and 255. It is random, and
b = randint(0,255)  # changes every time the loop runs  
ji.pencolor(r,g,b)

jiclone = []

degree = 0
for x in range(12):
    jiclone.append(ji.clone())
    jiclone[x].left(degree)
    degree = degree + 30
ji.hideturtle()


for x in range(3):
    for clone in jiclone:   # 1st pattern  
        r = randint(0,255)  # makes variables r,g,b whose value is an integer,
        g = randint(0,255)  # which is between 0 and 255. It is random, and
        b = randint(0,255)  # changes every time the loop runs  
        clone.pencolor(r,g,b)          
        clone.right(90)
        clone.forward(30)
        clone.right(60)
        clone.forward(50)
        clone.left(20)
        
for clone in jiclone:
    clone.goto(0,0)        # BACK TO ORIGIN
    clone.up()
    clone.forward(80)
    clone.down()

turtle.tracer(False)
for clone in jiclone:       # 2nd pattern
    for x in range (180):
        clone.left(2)
        clone.forward(1)
turtle.tracer(True)

ji.showturtle()     #CIRCLES
ji.up()
ji.forward(120)
ji.left(90)
ji.down()
ji.pensize(2)
ji.circle(120)
ji.right(90)
ji.up()
ji.forward(10)
ji.left(90)
ji.down()
ji.pensize(0.5)
ji.circle(130)
ji.right(90)
ji.up()
ji.forward(20)
ji.left(90)
ji.down()
ji.pensize(4)
ji.circle(150)
ji.right(90)
ji.hideturtle()

turtle.tracer(False)
for clone in jiclone:       # 3rd pattern
    for x in range(90):
        clone.left(1)
        clone.forward(1)
    
    clone.left(90)

    for x in range(90):
        clone.right(1)
        clone.forward(1)
turtle.tracer(True)

for clone in jiclone:       #4th pattern
    clone.up()
    clone.forward(40)
    clone.down()
    turtle.tracer(False)
    for x in range(4):
        for x in range(75):
            clone.left(1)
            clone.forward(1)
        clone.left(90)
        for x in range(75):
            clone.left(1)
            clone.forward(1)
    turtle.tracer(True)

    clone.up()          #adjustment
    clone.left(180)
    clone.forward(20)
    clone.down()

    clone.up()          #adjustment
    clone.right(90)
    clone.forward(50)

for clone in jiclone:
    clone.down()
    clone.pensize(2)
    turtle.tracer(False)
    for x in range(230):
        clone.left(1)
        clone.forward(1)
    turtle.tracer(True)

    clone.hideturtle()
turtle.done()
