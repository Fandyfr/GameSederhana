###
# APP Version: v0.1
# Buatan Fandy Fathurrohman
###

import os
import turtle
from random import choice, random
from turtle import *
from freegames import vector

"""Python Bahasa Jaksel"""
selesai = done

"""Display didalam Permainan"""
layar = turtle.Screen()
layar.title("Permainan Sederhana Ping Pong By Fandyfr")
layar.setup(600, 600)
layar.bgcolor("white")


def value():
    return (3 + random() * 2) * choice([1, -1])

bola = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}

def Gerakan(player, change):
    state[player] += change

def Kotak(x, y, width, height):
    up()
    goto(x,y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    """Gerakan Pingpong Dan Gambaran Game"""
    clear()
    Kotak(-200, state[1], 10, 50)
    Kotak(190, state[2], 10, 50)

    bola.move(aim)
    x = bola.x
    y = bola.y

    up()
    goto(x, y)
    dot(10)
    update()
    """System Gerakan Bola"""
    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        rendah = state[1]
        tinggi = state[1] + 50
        if rendah <= y <= tinggi:
            aim.x = -aim.x
        else:
            return
    if x > 185:
        rendah = state[2]
        tinggi = state[2] + 50
        if rendah <= y <= tinggi:
            aim.x = -aim.x
        else:
            return
        
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: Gerakan(1, 20), 'w')
onkey(lambda: Gerakan(1, -20), 's')
onkey(lambda: Gerakan(2, 20), 'i')
onkey(lambda: Gerakan(2, -20), 'k')
draw()
selesai()