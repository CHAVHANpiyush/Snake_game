from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            data_score=data.read()
        self.highscore = int(data_score)
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.highscore}",align="center",font=(" Courier",24,"normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center", font=("Courier", 24, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}",align="center",font=("Courier",24,"normal"))

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt",mode="w") as data:
                data.write(str(self.score))
            self.highscore=self.score
        self.score=0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center",font=("Courier",24,"normal"))
