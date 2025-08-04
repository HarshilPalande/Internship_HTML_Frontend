print("Mihir Satardekar")

import turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

turtle.bgcolor('black')
turtle.speed(0)
turtle.tracer(5)

for i in range(360):
    turtle.color(colors[i % 7])
    turtle.circle(100)
    turtle.left(10)

turtle.update()
turtle.done()
