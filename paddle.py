from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.color("white")

    def left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())

    def right(self):
        if self.xcor() < 350:
            new_x = self.xcor() + 10
            self.goto(new_x, self.ycor())