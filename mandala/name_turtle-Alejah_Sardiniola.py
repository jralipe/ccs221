import turtle

window=turtle.Screen()
window.bgcolor("#25424C")
l=turtle.Turtle()
l.ht()
l.speed(5)
l.width(8)
l.up()
l.setposition(-150,60)
l.color("#FFA45B")

# Letter a
l.down()
l.left(70) 
l.backward(80)
l.backward(50)
l.up()
l.left(0)
l.forward(80)
l.forward(50)
l.down()
l.right(140) 
l.forward(80)
l.forward(50)
l.up()
l.backward(50)
l.down()
l.left(180) 
l.left(70) 
l.forward(55)
l.up()
l.right(100)
l.right(40)
l.forward(120)
l.down()

#Letter L
def letterL():
    l.right(130)
    l.forward(120)
    l.left(90)
    l.forward(70)
letterL()

#Letter E
l.up()
l.right(-80)
l.forward(120)
l.down()
l.right(170)
l.forward(120)
l.left(90)
l.forward(70)
l.up()
l.left(90)
l.forward(60)
l.down()
l.left(90)
l.forward(70)
l.up()
l.right(90)
l.forward(60)
l.down()
l.right(90)
l.forward(70)
l.up()

#Letter J
l.right(0)
l.forward(120)
l.down()
l.right(90)
l.forward(80)
for x in range(27):
    l.right(7)
    l.forward(5)
l.up()
l.right(15)
l.forward(76)
l.down()
l.right(66)
l.forward(80)








