import turtle

colors= ["white","black"]
t=turtle.Pen()
t.speed(10)
t.pensize(5)
turtle.bgcolor("gray")
inverted=[-1,1]
#making an outer circle
y=1
x=1
t.up()
t.goto(0,-200)
t.down()
while x <3:
    t.color(colors[x%2])
    t.begin_fill()
    t.circle(200/y)
    t.end_fill()
    x+=1
    y+=1
    t.up()
    t.goto(0,0)
    t.down()
#putting an semi circle to form yin yang
a=3
b=1
while a < 5:
    t.color(colors[a%3])
    t.up()
    t.setposition(0,-200)
    t.down()
    t.begin_fill()
    t.circle(200*inverted[b%2]/b,-180*inverted[b%2])
    t.end_fill()
    a+=1
    b+=1
#making of the dots
d=1
while d < 3:
    t.up()
    t.goto(0,75*inverted[d%2])
    t.down()
    t.color(colors[d%2])
    t.begin_fill()
    t.circle(25*inverted[d%2])
    t.end_fill()
    d+=1
#outside design
for i in range(36):
    t.up()
    t.goto(0,0)
    t.down
    t.color(colors[i%2])
    t.up()
    t.forward(220)
    t.right(90)
    t.forward(10)
    t.down()
    t.left(180)
    t.forward(20)
    t.up()
    t.goto(0,0)
    t.down()
    t.left(20)
for i in range(36):
    t.up()
    t.goto(0,0)
    t.down
    t.color(colors[i%2])
    t.up()
    t.forward(240)
    t.right(90)
    t.forward(10)
    t.down()
    t.left(180)
    t.forward(20)
    t.up()
    t.goto(0,0)
    t.down()
    t.left(20)
for i in range(36):
    t.up()
    t.goto(0,0)
    t.down
    t.color(colors[i%2])
    t.up()
    t.forward(260)
    t.right(90)
    t.forward(10)
    t.down()
    t.left(180)
    t.begin_fill()
    t.forward(20)
    t.right(120)
    t.forward(20)
    t.right(120)
    t.forward(20)
    t.end_fill()
    t.up()
    t.goto(0,0)
    t.down()
    t.left(20)
t.up()
t.goto(0,200)
t.down()
t.circle(-200)
turtle.done()
