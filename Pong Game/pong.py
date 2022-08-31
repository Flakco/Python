import turtle
import pygame
from pygame import mixer

pygame.init()
a = mixer.Sound("pong.mp3")
mixer.init()

ventana = turtle.Screen()
ventana.title("PONG GAME")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

#scores
scorea = 0
scoreb = 0

#paleta1
paleta1 = turtle.Turtle()
paleta1.speed(0)
paleta1.shape("square")
paleta1.color("white")
paleta1.shapesize(stretch_wid=5, stretch_len=1)
paleta1.penup()
paleta1.goto(-350, 0)

#paleta2
paleta2 = turtle.Turtle()
paleta2.speed(0)
paleta2.shape("square")
paleta2.color("white")
paleta2.shapesize(stretch_wid=5, stretch_len=1)
paleta2.penup()
paleta2.goto(+350, 0)

#pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelotadx = 0.2
pelotady = 0.2

#score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Jugador 1: {scorea}  Jugador 2: {scoreb}", align="center", font=("arial", 14, "bold"))


#funciones
def paleta1arriba():
        y = paleta1.ycor()
        y += 10
        paleta1.sety(y)

def paleta1abajo():
        y = paleta1.ycor()
        y -= 10
        paleta1.sety(y)

def paleta2arriba():
        y = paleta2.ycor()
        y += 10
        paleta2.sety(y)

def paleta2abajo():
        y = paleta2.ycor()
        y -= 10
        paleta2.sety(y)

#teclas apretadas
ventana.listen()
ventana.onkeypress(paleta1arriba, "Up")
ventana.onkeypress(paleta1abajo, "Down")
ventana.onkeypress(paleta2arriba, "w")
ventana.onkeypress(paleta2abajo, "s")

#loop
while True:
    ventana.update()
    
    #movimiento pelota
    pelota.setx(pelota.xcor() + pelotadx)
    pelota.sety(pelota.ycor() + pelotady)

    #limite ventana
    if pelota.ycor() >= 290:
        pelota.sety(290)
        pelotady *= -1
        a.play()

    if pelota.ycor() <= -290:
        pelota.sety(-290)
        pelotady *= -1
        a.play()

    if pelota.xcor() >= 390:
        pelota.goto(0,0)
        pelotadx *= -1
        scorea += 1
        score.clear()
        score.write(f"Jugador 1: {scorea}  Jugador 2: {scoreb}", align="center", font=("arial", 14, "bold"))

    if pelota.xcor() <= -390:
        pelota.goto(0,0)
        pelotadx *= -1
        scoreb += 1
        score.clear()
        score.write(f"Jugador 1: {scorea}  Jugador 2: {scoreb}", align="center", font=("arial", 14, "bold"))

    #rebote
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta2.ycor() + 50 and pelota.ycor() > paleta2.ycor() - 50):
        pelota.setx(340)
        pelotadx *= -1
        a.play()

    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta1.ycor() + 50 and pelota.ycor() > paleta1.ycor() - 50):
        pelota.setx(-340)
        pelotadx *= -1
        a.play()
