import turtle

window = turtle.Screen()
window.bgcolor("#333333")
carla=turtle.Turtle()
carla.color("pink")

#Letter C

carla.left(180) #angle
carla.forward(30) #length

for x in range(20):
    carla.left(10)
    carla.forward(5)
    carla.forward(5)
    carla.forward(5)

carla.penup()

#Letter A

carla.forward(20)
carla.pendown()
carla.left(45)
carla.forward(170)
carla.right(135)
carla.forward(170)
carla.right(180)
carla.forward(67.5)
carla.left(70)
carla.forward(80)
carla.right(180)
carla.forward(80)
carla.penup()

#Letter R

carla.forward(50)
carla.right(90)
carla.forward(62)
carla.right(180)
carla.pendown()
carla.forward(155)
carla.right(90)
carla.forward(70)

for x in range(9): 
    carla.right(10) #curve angle
    carla.forward(5)

carla.forward(30)

for x in range(9):
    carla.right(10) #curve down
    carla.forward(5)

carla.forward(65)
carla.right(180)
carla.forward(70)
carla.right(65)
carla.forward(80)

carla.penup()

#Letter L
carla.left(70)
carla.forward(20)
carla.left(85)
carla.pendown()
carla.forward(150)
carla.right(180)
carla.forward(150)
carla.left(90)
carla.forward(100)
carla.penup()


turtle.done()