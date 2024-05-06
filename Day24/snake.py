from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT =0

class Snake:
    def __init__(self) -> None:
        self.starting_positon = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]
        
    def make_snake(self):
        for position in self.starting_positon:
            self.add_segment(position)            
    
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend(self):
        pos = self.segments[-1].position()
        self.add_segment(pos)
            
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        
        self.segments.clear()
        self.make_snake()
        self.head = self.segments[0]
        