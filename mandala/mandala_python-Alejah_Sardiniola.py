import turtle
window=turtle.Screen()
window.bgcolor("black")
a=turtle.Turtle()
a.ht()
#center circle
a.down()
a.speed(90)
a.color("#25424c")
a.begin_fill()
a.circle(15)
a.end_fill()

#3 dots
a.up()
a.right(90)
a.forward(7)
a.down()
def d_dots():
    def dots_1st_lvl(x):
        a.color("#ffebdb")
        a.dot(x)
    dots_1st_lvl(3)
    def spacing(n):
        a.up()
        a.forward(n)
        a.down()
    spacing(6.5)
    dots_1st_lvl(6)
    spacing(9.5)
    dots_1st_lvl(9)
d_dots()

#back to the center of the main circle
def back_to_main(n):
    a.up()
    a.right(180)
    a.forward(n)

back_to_main(40)

#2nd tower
def tower(z):
    a.left(45)
    a.forward(z)
    d_dots()
    back_to_main(40)
tower(23)
a.speed(9000)
for i in range(6):
    tower(23)

#3rd lvl=====================================
a.up()
a.right(180)
a.forward(60)
a.down()
a.color("#fb770d")

a.dot(12)#1
def lvl3(n):
    a.up()
    a.right(180)
    a.forward(60)
    a.right(n)
    a.forward(60)
    a.down()
    a.dot(4)
def lvl3b(n):
    a.up()
    a.right(180)
    a.forward(60)
    a.right(n)
    a.forward(60)
    a.down()
    a.dot(12)

for i in range(16):
    lvl3(-168.75)
    lvl3b(-168.75)

#4th lvl=============================
a.color("#ffa45b")
a.up()
a.right(180)
a.forward(60)
a.right(135)
a.forward(75)
a.dot(9)
a.forward(20)
a.dot(22)

back_to_main(170)
def blue_dots():
    a.dot(9)
    a.forward(20)
    a.dot(22)
blue_dots()
def tower2():
    back_to_main(95)
    a.left(45)
    a.forward(75)
    blue_dots()
    
for i in range(7):
    tower2()

#5th lvl=============================
a.up()
a.color("#ffebdb")
a.forward(20)
a.down()
a.right(90)
a.width(3)
for i in range(72):
    a.right(0)
    a.forward(5)
    a.right(5)
    a.forward(5)
    
#6th lvl============================
a.up()
a.color('#fb770d')
a.left(90)
a.forward(10)
a.down()

#square
a.right(0)
a.forward(30)

def square_leg(n):
    a.right(90)
    a.forward(n)
a.begin_fill()        
square_leg(10)
square_leg(30)
square_leg(10)
a.end_fill()

#end of square 1
def square():
    a.up()
    a.left(90)
    a.forward(125)

    a.left(170)
    a.forward(125)
    a.down()
    a.right(0)
    a.begin_fill()
    a.forward(30)
    square_leg(10)
    square_leg(30)
    square_leg(10)
    a.end_fill()

for i in range (35):
    square()

#7th lvl================================
a.color("#faf3e3")
a.width(3)

a.up()
a.right(90)
a.forward(40)
def circle_line(ranges, angle):
    a.down()
    a.right(90)

    for i in range(ranges): 
        a.right(0)
        a.forward(5)
        a.right(angle) 
        a.forward(5)
circle_line(105, 3.5)

#8th lvl=============================
a.color("#25424c")

def next_line_space():
    a.up()
    a.left(90)
    a.forward(10)
next_line_space()

circle_line(110, 3.3)
#9th lvl=============================
next_line_space()
circle_line(120, 3.1)
#10th lvl=============================
a.up()
a.color("#ffa45b")
a.left(85)
a.forward(20)
a.down()
a.dot(20)

a.up()
a.right(90)
a.forward(30)
a.down()
a.dot(20)

def dots10():
    a.up()
    a.right(8.5)
    a.forward(30)
    a.down()
    a.dot(20)

for i in range (40):
    dots10()
#11th lvl=============================
a.color("#25424c")
a.up()
a.left(0)
a.forward(80)
a.left(90)
a.forward(16)

a.down()
a.dot(35)

a.up()
a.right(120)
a.forward(60)
a.down()
a.dot(35)

def dots11():
    a.up()
    a.right(14.6) #14.6
    a.forward(60) #60
    a.down()
    a.dot(35)
for i in range(23):
    dots11()




