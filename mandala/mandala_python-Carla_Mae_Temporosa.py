import turtle

window = turtle.Screen()
window.bgcolor("#333333")
carla = turtle.Turtle()
carla.color("pink")
carla.speed(999999999999999999999999999999999999999999999999*10000000000000000000000000000000)


carla2 = turtle.Turtle()
carla2.color("yellow")
carla2.goto(90,40)
carla2.speed(999999999999999999999999999999999999999999999999*10000000000000000000000000000000)

carla3 = turtle.Turtle()
carla3.color("white")
carla3.goto(90,40)
carla3.speed(999999999999999999999999999999999999999999999999*10000000000000000000000000000000)

distance = 20
sides = 50

carla.hideturtle()
carla2.hideturtle()
carla3.hideturtle()

#turtle.tracer(False) #// enable for faster animation
for x in range(150):
    
    carla2.forward(distance /sides + x)
    carla2.left(100)
    
    carla.backward(distance / sides + x)
    carla.right(100)
    carla.forward(30)
    for x in range(5):
        carla.right(10)
        carla.forward(10)
    for x in range(5):
        carla.right(15)
        carla.backward(distance / sides + x)
    carla.begin_fill()
    carla.circle(10)
    carla.end_fill()
    carla.right(105)
    carla.forward(60)
   
    carla3.right(60)
    carla3.forward(30)
    carla3.right(45)
    for x in range(5):
        carla3.forward(3)

    carla3.right(90)
    for x in range(5):
        carla3.forward(distance / sides + x)
    carla3.right(65)
    carla3.forward(35)

#turtle.tracer(True)
 

turtle.done()