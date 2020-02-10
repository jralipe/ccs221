import turtle

window=turtle.Screen()
window.bgcolor("white")

#turtle.ht()
#turtle.dot(20, "black")

#FIRST LAYER
t5=turtle.Turtle()
t5.pensize(2)
t5.speed(0)
t5.fillcolor("#071F33")
t5.begin_fill()
for m in range(1):
    t5.home()
    for n in range(12):
       t5.penup()
       t5.right(40)
       t5.pendown()
       for o in range(4):
           t5.right(90)
           t5.forward(240)
t5.end_fill()

#SECOND LAYER
t4=turtle.Turtle()
t4.pensize(2)
t4.speed(0)
t4.fillcolor("#0E3F66")
t4.begin_fill()
for j in range(1):
    t4.home()
    for k in range(5):
        t4.penup()
        t4.right(30)
        t4.pendown()
        for l in range(6):
            t4.circle(150)
            t4.right(60)
t4.end_fill()

#THIRD LAYER
t3=turtle.Turtle()
t3.pensize(2)
t3.speed(0)
t3.fillcolor("#1766A6")
t3.begin_fill()
for g in range(1):
    t3.home()
    for h in range(12):
       t3.penup()
       t3.right(60)
       t3.pendown()
       for i in range(4):
           t3.right(90)
           t3.forward(200)
t3.end_fill()

#FOURTH LAYER
t2=turtle.Turtle()
t2.pensize(2)
t2.speed(0)
t2.fillcolor("#03A9F4")
t2.begin_fill()
for d in range(1):
    t2.home()
    for e in range(5):
        t2.penup()
        t2.right(90)
        t2.pendown()
        for f in range(6):
            t2.circle(100)
            t2.right(30)
t2.end_fill()

#FIFTH LAYER
t=turtle.Turtle()
t.pensize(2)
t.speed(0)
t.fillcolor("#80C6FF")
t.begin_fill()
for a in range(1):
    t.home()
    for b in range(12):
       t.penup()
       t.right(30)
       t.pendown()
       for c in range(4):
           t.right(90)
           t.forward(100)
t.end_fill()

#SIXTH LAYER
t=turtle.Turtle()
t.pensize(2)
t.speed(0)
for P in range(1):
    t.home()
    for Q in range(5):
        t.penup()
        t.right(90)
        t.pendown()
        for R in range(6):
            t.circle(20)
            t.right(30)
    
turtle.done()


