from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0 
        self.r_score = 0
        self.update_board()
        
    def update_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score,align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score,align=ALIGNMENT, font=FONT)
    
    def r_point(self):
        self.r_score += 1
        self.update_board()   
    
    def l_point(self):
        self.l_score += 1
        self.update_board()