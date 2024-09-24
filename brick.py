from turtle import Turtle
import random as r

COLORS = ['red', 'blue', 'yellow', 'pink', 'green']

class Brick(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(r.choices(COLORS))
        

    def remove(self):
        self.hideturtle()