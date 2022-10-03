from turtle import *
import random
color = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for n in range(60):
    pencolor(colors [n % 6])
    width(n / 100 + 1)
    forward(n)
    left(59)
    pencolor(colors [n % 6])

    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))

    for i in range(6):
        circle(circle_size)
        left(60)
