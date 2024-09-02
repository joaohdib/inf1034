# -*- coding: utf-8 -*-

#João Henrique Roseira Dib
#2210993
#01.a INF1034

import turtle

t = turtle.Turtle()

#eixo x
t.clear()
t.penup()
t.setpos(-470,0)
t.pendown()
t.forward(940)
t.stamp()

#eixo y
t.back(470)
t.left(90)
t.forward(400)
t.stamp()
t.right(180)
t.forward(800)

#quadrado
t.penup()
t.goto(200,200)
t.pendown()
for i in range(4):
    t.forward(100)
    t.right(90)
t.penup()

#triangulo
t.forward(270)
t.right(90)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)
t.penup()

#circulo
t.forward(400)
t.pendown()
t.circle(60)
t.penup()


#espiral
t.right(90)
t.forward(230)
t.right(90)
t.pendown()

n = 5
for i in range(50):
    t.forward(n)
    n += 1
    t.right(45)


turtle.done()

