from turtle import *

command = input("What do you like to see?")
match command.split
    case[1]: #Simple square
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
    case[2]: #Simple spiral
        for i in range(500): # this "for" repeat these function 500 times
        forward(i)
        left(91)


