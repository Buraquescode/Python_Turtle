# Python_Spiral
import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral Pattern")

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)
my_turtle.width(2)

# Define the number of circles and the increment factor for color
num_circles = 100
color_increment = 1.0 / num_circles

# Draw the spiral pattern
for _ in range(num_circles):
    color = colorsys.hsv_to_rgb(_ * color_increment, 1.0, 1.0)
    my_turtle.color(color)
    my_turtle.circle(100)
    my_turtle.left(10)

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open until it's closed by the user
turtle.mainloop()
