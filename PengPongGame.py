# import turtil moduls
import time
import turtledemo.clock
# import pygame
# time.get_clock_info()
# score_time = pygame.time.get_ticks()
# pygame.
from  turtle import *
windo = Screen()
windo.title("Bing Bong")
windo.bgcolor("black")
windo.setup(width=800,height=600)
windo.tracer(0)
# ========== mahtrb1 =======
mahtrb1 = Turtle()
mahtrb1.shape("square")
mahtrb1.shapesize(stretch_wid=5,stretch_len=1)
mahtrb1.color("blue")
mahtrb1.penup()
mahtrb1.goto(-350 , 0)
# ========== mahtrb2 =======
mahtrb2 = Turtle()
mahtrb2.shape("square")
mahtrb2.shapesize(stretch_wid=5,stretch_len=1)
mahtrb2.color("blue")
mahtrb2.penup()
mahtrb2.goto(350 , 0)
# ========== mahtrb1 =======
# score_time = Turtle.time.get_ticks()

boll = Turtle()
boll.shape("square")
boll.color("white")
boll.penup()
boll.goto(0 , 0)
boll.dx = 0.3
boll.dy = 0.3

scor1 = 0 
scor2 = 0 
score = Turtle ()
score.speed(0)
score.color("white")
score.penup()
# score.hideturtle()
score.goto(0,260)
score.write(f"playr 1 : {scor1}  playr 2 : {scor2} " ,font = "courier",align="center" )
# ball_time = turtledemo.clock.tick()
# boll.getturtle().
def mathrb1_up (): 
    if mahtrb1.ycor() < 250 : 

        y = mahtrb1.ycor()
        y += 20 
        mahtrb1.sety(y)
    else: 
        mahtrb1.sety(250)
def mathrb1_down (): 
    if mahtrb1.ycor()> -250 : 

        y = mahtrb1.ycor()
        y -= 20 
        mahtrb1.sety(y)
    else:
        mahtrb1.sety(-250)
def mathrb2_up (): 
    if mahtrb2.ycor() < 250 : 

        y = mahtrb2.ycor()
        y += 20 
        mahtrb2.sety(y)
    else: 
        mahtrb2.sety(250)
def mathrb2_down (): 
    if mahtrb2.ycor()> -250 : 

        y = mahtrb2.ycor()
        y -= 20 
        mahtrb2.sety(y)
    else:
        mahtrb2.sety(-250)
windo.listen()
windo.onkeypress(mathrb1_up,"w")
windo.onkeypress(mathrb1_down,"s")
windo.onkeypress(mathrb2_up,"Up")
windo.onkeypress(mathrb2_down,"Down")

while True : 
    windo.update()
    boll.setx(boll.xcor() + boll.dx )
    boll.sety(boll.ycor() + boll.dy )
    if boll.ycor() > 290 : 
        boll.dy *=-1
    if boll.ycor() < -290 : 
        boll.sety(-290)
        boll.dy *=-1
    if boll.xcor() > 390 :
        # turtledemo.clock.tick()
        # score_time
        boll.goto(0,0)
        # time.sleep(5)
        # time
        scor1+=1
        score.clear()
        score.write(f"playr 1 : {scor1}  playr 2 : {scor2} " ,font = "courier",align="center" )
    # time.sleep(5)
    if boll.xcor() < -390 :
        # turtledemo.clock.tick()
        # score_time
        boll.goto(0,0)
        # time.sleep(5)
        scor2+=1
        score.clear()
        score.write(f"playr 1 : {scor1}  playr 2 : {scor2} " ,font = "courier",align="center" )
    # time.sleep(5)
    # if scor1 > 0:
    #     time.sleep(5)
    # if scor2 > 0:
    #     time.sleep(5)
    # if boll.getscreen():
    #     boll = time.sleep(5)
    if (boll.xcor()> 340 and boll.xcor() < 350  ) and (boll.ycor()< mahtrb2.ycor() + 40 and boll.ycor()>mahtrb2.ycor() -40 ) :
        boll.setx(340)
        # turtledemo.clock.tick()
        boll.dx *=-1
        # time.sleep(5)
    if (boll.xcor()< -340 and boll.xcor() > -350  ) and (boll.ycor()< mahtrb1.ycor() + 40 and boll.ycor()>mahtrb1.ycor() -40 ) :
        boll.setx(-340)
        # turtledemo.clock.tick()
        boll.dx *=-1
        # time.sleep(5)
    # if scor1 > 0:
    #     time.sleep(5)
    # if scor2 > 0:
    #     time.sleep(5)