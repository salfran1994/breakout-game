import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from manage_bricks import BrickManager
from game_over import GameOver
import threading


screen = Screen()
screen.setup(height=400, width=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

def game(game_on):
    while game_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Bounce against the walls
        if ball.ycor() > 180:
            ball.bounce_y()
        
        #bounce on x
        if ball.xcor() > 380 or ball.xcor() < - 380:
            ball.bounce_x()

        if ball.ycor() < -160:
            game_on = game_over()
        #bounce on paddle
        elif ball.distance(pad) < 55 and ball.ycor() < -140:
            ball.bounce_y()
            if ball.x_move < 0 and ball.xcor() > pad.xcor():
                ball.bounce_x()
            elif ball.x_move > 0 and ball.xcor() < pad.xcor():
                ball.bounce_x()
        else:
            decition, brick = bricks.check_collision(ball)
            
            if decition:
                bricks.remove_brick(brick)
                ball.bounce_y()

def game_over():
    screen.clear()
    screen.bgcolor("black")
    GameOver()
    return False

game_on = True

pad = Paddle((0, -160))
ball = Ball()
bricks = BrickManager()
bricks.create_bricks()


screen.listen()
screen.onkey(pad.left, "Left")
screen.onkey(pad.right, "Right")


# This line will allow the ball run as a parallel process
paddle_thread = threading.Thread(target=game, kwargs={"game_on":game_on})
paddle_thread.start()


screen.exitonclick()