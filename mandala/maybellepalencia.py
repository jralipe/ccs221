import turtle
import math
import random
window = turtle.Screen()
window.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('red')
rotate=int(180)
def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def may(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(360/repeat)
may(s,200,10)
t1 = turtle.Turtle()
t1.speed(0)
t1.color('yellow')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def may(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
may(t1,160,10)
t2= turtle.Turtle()
t2.speed(0)
t2.color('blue')
rotate=int(180)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def may(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
        
may(t2,120,10)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen()
t.speed('fastest')
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59)
turtle.done()
#reference: https://youtu.be/Grc1-j4EvTk
