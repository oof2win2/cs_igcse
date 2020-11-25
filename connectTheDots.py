import turtle
import random
t = turtle.Turtle()
t.speed(10)

def write_points():
    turtle.tracer(100)
    turtle.colormode(255)
    t.up()
    for x in range(-250,251,50):
        for y in range(-250,251,50):
            t.goto(x,y)

            red, green, blue = abs(x), 0, abs(y)
            t.pencolor((red,green,blue))

            t.dot(5)
            t.write(str((x,y)))

def connect_points():
    turtle.tracer(100)
    write_points()
    t.up()
    t.goto(0,0) #starting point for drawing
    t.down()
    # turtle.tracer(1)
    # t.speed(2)
    x = 1
    for i in range(750):
        # x,y = [int(num) for num in input("Enter x, y: ").split(",")]
        x, y = random.randint(-255, 255), random.randint(-255, 255)
        red, green, blue = abs(x), 0, abs(y)
        t.pencolor((red,green,blue))
        print((x,y))
        t.goto((x,y))

connect_points()
t.wait()
