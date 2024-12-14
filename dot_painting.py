import colorgram
import turtle
import random

colors = colorgram.extract("C:\Downloads\psych.jpg",30)
#Extracting colours from the given image

rgb_list = []
for o in colors:
    rgb_list.append(tuple(o.rgb))
#list of all colours in RGB form

my_turtle = turtle.Turtle()
#creating turtle object

my_turtle.hideturtle()
#hiding the turtle arrow

scr = turtle.Screen()
#setting up screen

scr.colormode(255)
#setting color mode to RGB
my_turtle.penup()
#avoiding drawing of lines

my_turtle.speed("fastest")
#Setting speed of turtle

def painting(w,h): #defining function
    my_turtle.goto(-w*(50/2),-h*(50/2))
    #dimensions of the corner

    while my_turtle.position()[1] != (h*(50/2)):
    #While turtle is not at top corner

        while my_turtle.position()[0] != w*(50/2):
        #while turtle is not a the end of the line

            my_turtle.dot(20,random.choice(rgb_list))
            #Draw a dot with a random colour

            my_turtle.forward(50)
            #Move forward to the next point

        my_turtle.goto((-w*50/2),my_turtle.position()[1]+50)
        #Turtle going to start of next line
#hidind the turtle arrow

painting(5,6)
#calling the function

scr.exitonclick()
#exit the window