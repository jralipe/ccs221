from turtle import*
import turtle


window = turtle.Screen()
window.bgcolor("#000000")
j = turtle.Turtle ()
j.color("pink")
j.width(5)
j.speed(0)
B = 1 
BOX_WIDTH, BOX_HEIGHT=50,100
WIDTH, HEIGHT = BOX_WIDTH - B * 2, BOX_HEIGHT - B * 2

j.up()
j.setpos(-170,30)
j.down()

def J (j):
    j.forward(WIDTH)#j
    j.right(180)
    j.forward(WIDTH/2)
    j.left(90)
    j.forward(HEIGHT)
    j.right(90)
    j.forward(WIDTH/2)
    j.right(90)
    j.forward(HEIGHT/2)

def A(j):
    j.up()
    j.right (90)#space A
    j.forward(WIDTH + 10)
    j.left(90)
    j.forward(HEIGHT/2)#space end
    j.down()
    j.right(90)
    j.forward(WIDTH)
    j.right(180)
    j.forward(WIDTH)
    j.left(90)
    j.forward(HEIGHT)
    j.right(180)
    j.forward(HEIGHT/2)
    j.right(90)
    j.forward(WIDTH)
    j.left(90)
    j.forward(HEIGHT/2)
    j.left(180)
    j.forward(HEIGHT)

def S(j):
    j.up()#space S
    j.left(90)
    j.forward(10)
    j.left(90)
    j.forward(HEIGHT)
    j.right(90)
    j.forward(WIDTH)#space end 
    j.down()
    j.right(180)
    j.forward(WIDTH)
    j.left(90)
    j.forward(HEIGHT/2)
    j.left(90)
    j.forward(WIDTH)
    j.right(90)
    j.forward(HEIGHT/2)
    j.right(90)
    j.forward(WIDTH)
    
def P(j):
    j.up() #space P
    j.right(180)
    j.forward(WIDTH+10)#end
    j.down()
    j.left(90)
    j.forward(HEIGHT)
    j.right(90)
    j.forward(WIDTH)
    j.right(90)
    j.forward(HEIGHT/2)
    j.right(90)
    j.forward(WIDTH)

def E(j):
    j.up() #space E
    j.right(180)
    j.forward(WIDTH+10)
    j.left(90)
    j.forward(HEIGHT/2)
    j.right(90)
    j.forward(WIDTH)#end
    j.down()
    j.right(180)
    j.forward(WIDTH)
    j.left(90)
    j.forward(HEIGHT)
    j.left(90)
    j.forward(WIDTH)
    j.up() #Space E
    j.left(90)
    j.forward(HEIGHT/2)
    j.left(90)
    j.forward (WIDTH)#end
    j.down()
    j.left(180)
    j.forward(WIDTH)
def R(j):
    j.up()#space R
    j.forward(10)
    j.left(90)
    j.forward(HEIGHT/2)#end
    j.down()
    j.right(90)
    j.forward(WIDTH)
    j.right(90)
    j.forward(HEIGHT/2)
    j.right(90)
    j.forward(WIDTH)
    j.right(90)
    j.forward(HEIGHT/2)
    j.right(180)
    j.forward(HEIGHT)
    j.up()
    j.left(90)
    j.forward(WIDTH)
    j.down()
    j.left(125)
    j.forward(60)
    j.up()
    j.forward(200)

J(j),A(j),S(j),P(j),E(j),R(j)
turtle.done( )
 
