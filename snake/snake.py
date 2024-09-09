import turtle
screen=turtle.Screen()
t=turtle.Turtle()
t.hideturtle()
t.color("white")
t.penup()
t.goto(0,0)
UP=90
DOWN=270
RIGHT=0
LEFT=180
MOVE_DIST=20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
color_list =[(240, 242, 245), (223, 236, 228), (236, 230, 216), 
(140, 176, 207), (26, 107, 159), (237, 225, 235), (209, 161, 111),
(144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), 
(229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), 
(172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), 
(240, 204, 2), (1, 102, 119), (50, 150, 109), (172, 212, 172), 
(221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]
import random

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.paused=False
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_seg(position)

    def add_seg(self,position):
        new_turtle = turtle.Turtle(shape="circle")
        turtle.colormode(255)
        new_turtle.color(random.choice(color_list))
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_seg(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)        
    
    def up(self):
        if self.segments[0].heading()!= DOWN:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()!= UP:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading()!= LEFT:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading()!= RIGHT:
            self.segments[0].setheading(180)

    def pause(self):
        self.paused= not self.paused
        if self.paused:
            t.write(f"PAUSED", align="center", font=("Courier", 24, "normal"))
        else:
            t.clear()
            print("Game resumed")
    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()