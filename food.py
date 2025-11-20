from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        randome_x=random.randint(-280, 280)
        randome_y=random.randint(-280, 280)
        self.goto(randome_x,randome_y)
        self.refresh()

    def refresh(self):
        randome_x=random.randint(-280, 280)
        randome_y=random.randint(-280, 280)
        self.goto(randome_x,randome_y)
