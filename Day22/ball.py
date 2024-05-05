from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = 0
        self.y_pos = 0
        self.x_step = 10
        self.y_step = 10
        self.move_speed = 0.1
        self.up_down = "up"
        self.shape("circle")
        self.color("white")
        self.penup()
        
    def move(self):
        self.x_pos += self.x_step
        self.y_pos += self.y_step
        self.goto(self.x_pos, self.y_pos)
        
    def bounce(self):
        self.y_step *= -1
    
    def bounce_bar(self):
        self.x_step *= -1
        self.move_speed *= 0.9
        
    
    def reset_position(self):
        self.x_pos = 0
        self.y_pos = 0
        self.goto(self.x_pos, self.y_pos)
        self.bounce_bar()
        self.move_speed = 0.1