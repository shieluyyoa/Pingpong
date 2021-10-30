from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time


pingpong = Turtle()

paddle = Turtle()


pingpong_screen = Screen()
pingpong_screen.setup(800,600)
pingpong_screen.bgcolor("black")
pingpong_screen.tracer(0)

user_paddle = Paddle(350,0)
ai_paddle = Paddle(-350,0)

new_ball = Ball()




pingpong_screen.listen()

pingpong_screen.onkeypress(user_paddle.moveup,"a")
pingpong_screen.onkeypress(user_paddle.movedown,"d")

pingpong_screen.onkeypress(ai_paddle.moveup,"q")
pingpong_screen.onkeypress(ai_paddle.movedown,"e")



game_on = True



while game_on:
    
    pingpong_screen.update()
    
    new_ball.move()

    if new_ball.ycor() > 290 or new_ball.ycor() < -290:
        new_ball.bounce(1,-1)
    
    if new_ball.xcor() > 390 or new_ball.xcor() < -390:
        new_ball.bounce(-1,1)
    
    if new_ball.distance(user_paddle) <= 58 and new_ball.xcor() >= 340 :
        new_ball.bounce(-1,1)

    time.sleep(0.02)

pingpong_screen.exitonclick()


