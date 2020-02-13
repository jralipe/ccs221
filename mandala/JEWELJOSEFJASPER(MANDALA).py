from turtle import*

pencolor('black')
bgcolor('pink')
speed(0)
width(2)


while 10:
    rt(90)
    fillcolor('black')
    begin_fill()
    fd(60)
    rt(90)
    fd(60)
    rt(135)
    fd(80)
    end_fill()
    lt(45)
    fd(60)
    circle(80)
    lt(90)
    fd(100)
    up()
    fd(5)
    down()
    circle(50)
    rt(80)
    fd(20)
    fillcolor('black')
    begin_fill()
    circle(80,extent=160)
    end_fill()
    fd(50)
    circle(70)

    if abs(pos())<1:
        break

exitonclick()
