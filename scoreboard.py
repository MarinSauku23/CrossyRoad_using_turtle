from turtle import Turtle

FONT = ("Courier", 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color('black')
        self.penup()
        self.goto(-220, 260)
        self.write(arg=f"Level: {self.score}", align='center', font=FONT)
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"Level: {self.score}", align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.color('black')
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=FONT)
        self.hideturtle()
