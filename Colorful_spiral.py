import turtle as tur
import colorsys as cs
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
for i in range(300):
    tur.color(cs.hsv_to_rgb(i/300,0.5,1))
    tur.forward(i)
    tur.left(59)
tur.hideturtle()
tur.done()