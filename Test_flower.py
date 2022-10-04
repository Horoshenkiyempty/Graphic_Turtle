from turtle import *
t = Turtle()
bgcolor("black")
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange',]
#t.pencolor("purple")
t.speed(0)
for i in range(340):
    t.circle(190-i, 90)
    t.left(90)
    t.circle(190 - i, 90)
    t.left(18)
    if i > 190:
        t.pensize(3)
        t.pencolor("gray")
    else:
        t.pencolor(colors [i % 6])