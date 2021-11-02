from turtle import Turtle

class sb(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,150)

        self.color("white")
        self.write("0      0",False,align="center",font=("Arial",100,"normal"))
        self.ai_score = 0 
        self.user_score =0

    def ai(self):
        self.clear()
        self.ai_score += 1
        self.write(f"{self.ai_score}      {self.user_score}",False,align="center",font=("Arial",100,"normal"))

    def user(self):
        self.clear()
        self.user_score += 1
        self.write(f"{self.ai_score}      {self.user_score}",False,align="center",font=("Arial",100,"normal"))
                    