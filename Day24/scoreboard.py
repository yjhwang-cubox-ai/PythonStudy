from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}  high_score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def plus_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.update_highscore(self.high_score)
    
    def read_highscore(self):
        with open("0506/data.txt", mode="r") as file:
            high_score = file.read()
        return int(high_score)

    def update_highscore(self, new_highscore):
        with open("0506/data.txt", mode="w") as file:
            file.write(str(new_highscore))