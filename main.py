import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(2)
t.hideturtle()
t.penup()

for scale in range(11, 17):
    for i in range(120):
        angle = i * (math.pi * 2) / 120

        x = 16 * (math.sin(angle) ** 3) * scale
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale

        # Color arcoíris
        hue = (i / 120 + scale * 0.08) % 1
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)

        # Turtle usa valores RGB entre 0 y 1
        t.color(rgb)

        t.goto(x, y)
        t.write(
            "Te quiero Valbb",
            align="center",
            font=("Arial", 8, "bold")
        )

turtle.done()