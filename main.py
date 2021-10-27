from turtle import Turtle,Screen
from paddle import Paddle

pingpong = Turtle()

paddle = Turtle()


pingpong_screen = Screen()
pingpong_screen.setup(800,600)
pingpong_screen.bgcolor("black")
pingpong_screen.tracer(0)

user_paddle = Paddle(350,0)

ai_paddle = Paddle(-350,0)


pingpong_screen.listen()




pingpong_screen.onkeypress(user_paddle.moveup,"a")
pingpong_screen.onkeypress(user_paddle.movedown,"d")

pingpong_screen.onkeypress(ai_paddle.moveup,"q")
pingpong_screen.onkeypress(ai_paddle.movedown,"e")

game_on = True

while game_on:
    pingpong_screen.update()

pingpong_screen.exitonclick()


