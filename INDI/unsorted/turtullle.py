import turtle

turtle.speed(1)
def drawsqu(a,color):
    turtle.begin_fill()
    turtle.color(color)
    for i in range(4):
        move(a)
    turtle.end_fill()
def move(a):
    turtle.forward(a)
    turtle.left(90)
turtle.clear()
drawsqu(100,'red')
turtle.goto(130,130)
drawsqu(150,'green')