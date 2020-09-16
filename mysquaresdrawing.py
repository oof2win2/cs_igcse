import turtle
import random


t = turtle.Turtle()
turtle.tracer(0)
turtle.colormode(255)
t.color(0, 193, 234)
colors = ["red", "green", "blue"]


def getColour():
    r = random.randint(0, 150)
    g = random.randint(0, 20)
    b = random.randint(0, 255)
    return (r, g, b)


def shape(sidelen, sides):
    colour = getColour()
    # colour = (0, 193, 243)
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(sides):
        t.fd(sidelen)
        t.left(360 / sides)
    t.end_fill()


def square(sidelen):
    colour = getColour()
    # colour = (0, 193, 243)
    t.fillcolor(colour)
    t.begin_fill()
    for i in range(4):
        t.fd(sidelen)
        t.left(360 / 4)
    t.end_fill()


def multSquares(sidelen, num):
    for i in range(num):
        square(sidelen)


def getRandPos():
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    return (x, y)


def complexShape():
    while True:
        pos = getRandPos()
        t.color(getColour())
        t.penup()
        t.goto(pos[0], pos[1])
        t.pendown()
        square(random.randint(0, 400))


while True:
    # multSquares(100, 1000)
    complexShape()
turtle.mainloop()
