from turtle import Turtle
from turtle import Screen
import random

my_turtle = Turtle()
# Creating turtle object

scr = Screen()
#setting up the window

my_turtle.speed(0)
#setting turtle speed

my_turtle.pensize(2)
#thickness of the lines/dots/etc.

scr.colormode(255)
#setting screen color mode to RGB

def spiro(num): #function to make spirals
    for n in range(0,num): #for loop for number of circles
        my_turtle.pencolor((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
        #random colour selector for circle

        my_turtle.circle(100)
        #draw the circle

        my_turtle.right(360/num)
        #turtle angle change to start making the next circle
spiro(100)
#calling the function
scr.exitonclick()