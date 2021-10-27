from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.goto(xcor,ycor)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)



    def moveup(self):
        self.goto(self.xcor(),(self.ycor()+20))


    def movedown(self):
        self.goto(self.xcor(), (self.ycor()-20))

