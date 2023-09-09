from turtle import *

speed(40)
bgcolor("black")
pencolor("blue")

for i in range(150):
    right(i)
    circle(200,i)
    forward(i)
    right(90)
    forward(i)