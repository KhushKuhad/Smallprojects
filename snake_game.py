import turtle 
import random
import functools
import time

scr = turtle.Screen()
scr.setup(700,700)
scr.bgcolor('black')
scr.tracer(0)
tur = turtle.Turtle()
tur.shape("square")
tur.color('white')
tur.speed("slow")
tur.penup()

text_manager = turtle.Turtle(visible=False)
text_manager.pencolor('pink')
text_manager.penup()
text_manager.goto(-80,320)
score = 0
text_manager.write('SCORE : ',font=('Arial',20,'bold'))
text_manager.goto(40,320)
text_manager.write(score,font=('Arial',20,'bold'))

dot_spawner = turtle.Turtle('circle',500)
dot_spawner.color('turquoise')
dot_spawner.shapesize(0.5,0.5,1)
dot_spawner.penup()

segment_list = []
segment_list.append(tur)
for num in range(0,3):
    tut = tur.clone()
    segment_list.append(tut)
x=0
for t in segment_list:
    t.goto(x,0)
    x = x-20
game_on = True

def movement(key):

    if key == 'w':
        if segment_list[0].heading() != 270:
            segment_list[0].seth(90)
    elif key == 's':
        if segment_list[0].heading() != 90:
            segment_list[0].seth(270)
    elif key == 'a':
        if segment_list[0].heading() != 0:
            segment_list[0].seth(180)
    elif key == 'd':
        if segment_list[0].heading() != 180:
                segment_list[0].seth(0)

def myround(x, base=20):
    return base * round(x/base)

dot_spawner.goto(myround(random.randint(-320,320)),myround(random.randint(-320,320)))

while game_on:
    time.sleep(0.15)
    scr.update()

    for i in range(len(segment_list)-1,0,-1):
        new_x = segment_list[i-1].xcor()
        new_y = segment_list[i-1].ycor()
        segment_list[i].goto(new_x,new_y)
    segment_list[0].forward(20)

    if segment_list[0].xcor() > 340:
        segment_list[0].setx(-340)
    elif segment_list[0].xcor() < -340:
        segment_list[0].setx(340)

    if segment_list[0].ycor() > 340:
        segment_list[0].sety(-340)
    elif segment_list[0].ycor() < -340:
        segment_list[0].sety(340)

    for i in segment_list[1:]:
        if segment_list[0].distance(i) < 15:
            text_manager.home()
            text_manager.pencolor('red')
            text_manager.write('GAME OVER.',align='center',font=('Arial',40,'bold'))
            game_on = False
    
    if segment_list[0].distance(dot_spawner) < 10:
        score = score + 1
        dot_spawner.clear()
        text_manager.clear()
        text_manager.goto(-80,320)
        text_manager.write('SCORE : ',font=('Arial',20,'bold'))
        text_manager.goto(40,320)
        text_manager.write(score,font=('Arial',20,'bold'))
        dot_spawner.goto(myround(random.randint(-320,320)),myround(random.randint(-320,320)))
        segment_list.append(segment_list[0].clone())
    
    if segment_list[0].heading() == 0:
        scr.listen()
        for k in 'wasd':
            scr.onkey(functools.partial(movement, k), key=k)
    scr.update()
scr.exitonclick()