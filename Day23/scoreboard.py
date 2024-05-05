from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 0
        self.update_board()
    
    def update_board(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    
    def up_score(self):
        self.level += 1
        self.update_board()
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
