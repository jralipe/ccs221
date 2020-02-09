import turtle

julia=turtle.Turtle()
turtle.bgcolor("#EDABC7")
julia.shape("turtle")
julia.speed("fastest")
julia.width(2)
julia.pencolor("#7134BF")
juliaclone=[]
degree = 0
for i in range (10):
               juliaclone.append(julia.clone())
               juliaclone[i].left(degree)
               degree = degree + 45
julia.hideturtle()
for i in range(33):
    for clone in juliaclone:
        clone.right(90)
        clone.up()
        clone.forward(40)
        clone.right(60)
        clone.down()
        turtle.tracer(False)
        for i in range(160):
            clone.forward(2)
            clone.right(0.5)
        turtle.tracer(True)
        clone.left(130/100)
        turtle.tracer(False)        
turtle.done()

#Credits to Carlo Taleon for the idea of using Clone to have a shorter code
