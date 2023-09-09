from turtle import *
import colorsys
speed('fastest')
width(2)
hue = 0.0
for i in range(250):
    col = colorsys.hsv_to_rgb(hue,1,1)
    color(col)
    forward(i*2)
    right(121)
    hue +=0.005

done()