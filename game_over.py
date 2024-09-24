from turtle import Turtle


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color('deep pink')
        self.style = ('Courier', 30, 'italic')
        self.write('Game Over!!', font=('Courier', 30, 'italic'), align='center')
        self.hideturtle()
