import turtle

#pattern1
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(210)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    window.bgcolor('black')
    pattern = turtle.Turtle()
    pattern.color('red')
    pattern.pensize(4)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle

draw_art(25)


#pattern2
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    pattern = turtle.Turtle()
    pattern.color('orange')
    pattern.pensize(3)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle


#pattern3
draw_art(25)

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    pattern = turtle.Turtle()
    pattern.color('red')
    pattern.pensize(2)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle
    

draw_art(15)


#pattern4
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(180)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    pattern = turtle.Turtle()
    pattern.color('red')
    pattern.pensize(1)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle


draw_art(25)

#pattern5
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(130)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    window.bgcolor('black')
    pattern = turtle.Turtle()
    pattern.color('yellow')
    pattern.pensize(3)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle
    

draw_art(15)


#pattern6
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(125)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    pattern= turtle.Turtle()
    pattern.color('yellow')
    pattern.pensize(3)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle
    

draw_art(15)





#pattern7
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(50)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    pattern = turtle.Turtle()
    pattern.color('yellow')
    pattern.pensize(3)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle
    

draw_art(25)


#pattern8
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(55)
        some_turtle.right(90)


def draw_art(moving_angle):
    window = turtle.Screen()
    pattern = turtle.Turtle()
    pattern.color('orange')
    pattern.pensize(3)
    pattern.speed(0)

    circle = 0
    while circle < 360:
        draw_square(pattern)
        pattern.right(moving_angle)
        circle += moving_angle
    

draw_art(25)

#Credits to Amhed Koodh of Youtube.com.




















               
