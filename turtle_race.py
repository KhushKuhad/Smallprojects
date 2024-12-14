import turtle
import random

scr = turtle.Screen()
scr_width = 800
scr_height = 500
scr.setup(width=scr_width,height=scr_height)
user_guess = scr.textinput('GUESS','which colour will win?(red/yellow/green/blue/pink)')

a = turtle.Turtle()
a.shape("turtle")      #creating all coloured turtles
a.color('red')

b = turtle.Turtle()
b.shape("turtle")
b.color('blue')

c = turtle.Turtle()
c.shape("turtle")
c.color('green')

d = turtle.Turtle()
d.shape("turtle")
d.color('yellow')

e = turtle.Turtle()
e.shape("turtle")
e.color('pink')

top = scr_height/2-50      #start of positions

def takepos(tur_name):
    global top
    tur_name.penup()          #taking position of turtles
    tur_name.goto(-350,top)
    top = top- 100

takepos(a)
takepos(b)
takepos(c)
takepos(d)
takepos(e)

def run_race():
    a.forward(random.randint(0,30))
    b.forward(random.randint(0,30))
    c.forward(random.randint(0,30))     #Each turtle moves 1 step randomly
    d.forward(random.randint(0,30))
    e.forward(random.randint(0,30))

def win_check():
    for i in [a,b,c,d,e]:
        if i.position()[0]>=350:

            print(f"winner - {i.color()[0]}")
            ans = i.color()[0]         #checks for each letter a,b,c,d,e, if they reached finish line (350)
            if user_guess == i.color()[0]:
                print("right guess")
                return ans

while a.position()[0] <= 350 and b.position()[0] <= 350 and c.position()[0] <= 350 and d.position()[0] <= 350 and e.position()[0] <= 350:
    run_race()     #while all turtles are not at finish line yet
    final = win_check() 

if final == user_guess:
    print("YOU WIN")
else:
    print("YOU LOSE")

scr.exitonclick()