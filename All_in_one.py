from turtle import *
import random

command = input("What do you like to see?")
print("1. Simple square")
print("2. Simple spiral")
print("3. Colorful hexagon spiral")
print("4. A random blue flower")
print("5. Random colorful flower")
print("6. Flower")
print("7. Angle")

t = Turtle()
match command.split():
    case["1"]: #Simple square
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)

    case["2"]: #Simple spiral
        for i in range(500): # this "for" repeat these function 500 times
            forward(i)
            left(91)

    case["3"]: #Colorful hexagon spiral
        color = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for i in range(360):
            pencolor(colors [i % 6])
            width(i / 100 + 1)
            forward(i)
            left(59)

    case["4"]: #A random blue flower
        for n in range(60):
            penup()
            goto(random.randint(-400, 400), random.randint(-400, 400))
            pendown()

            red_amount   = random.randint( 0, 30) / 100.0
            blue_amount  = random.randint(50,100) / 100.0
            green_amount = random.randint( 0, 30) / 100.0

            pencolor((red_amount, green_amount, blue_amount))

            circle_size = random.randint(10, 40)
            pensize(random.randint(1, 5))

            for i in range(6):
                circle(circle_size)
                left(60)

    case["5"]: #Random colorful flower
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

    case["6"]: #Flower
        bgcolor("black")
        t.pencolor("purple")
        t.speed(0)
        for i in range(340):
            t.circle(190-i, 90)
            t.left(90)
            t.circle(190 - i, 90)
            t.left(18)
        if i > 190:
            t.pensize(3)

    case["7"]: #Angle
        for angle in range (0, 360 , 15):
            setheading(angle)
            forward(100)
            write(str(angle) + '°')
            backward(100)