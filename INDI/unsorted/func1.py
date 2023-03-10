import turtle

def move(a,b):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
def squaret(a,b):
    for i in range(2):
        move(a,b)
def squaretColor(a,b,color):
    turtle.color(color)
    turtle.begin_fill()
    squaret(a,b)
    turtle.end_fill()

turtle.speed(2)
squaretColor(15,40,'red')
turtle.goto(50,50)
squaretColor(50,30,'blue')
