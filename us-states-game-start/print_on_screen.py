import turtle
from turtle import Turtle
FONT = ("Courier", 7, "normal")


class PrintOnScreen:
    def __init__(self, state, position):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.position = position
        self.state = state
        self.turtle.goto(self.position)
        self.turtle.write(f"{self.state}", align="center", font=FONT)




