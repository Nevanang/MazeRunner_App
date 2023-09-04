import turtle, math
from changestart import SetStart

class OneVsOne(SetStart):
    def  __init__(self, start,end, walls):
        super().__init__(start,end,walls)
        self.flag = True
        self.start = start
        self.end = end
        self.walls = walls
        self.penup()
        self.hideturtle()
        self.shape("arrow")
        self.shapesize(0.5, 0.5, 1)
        self.color("orange")
        self.goto(start)
        self.showturtle()
        self.speed(2)

    def move_forward(self):
        super().move_forward()
        if self.pos() == self.end:
            return True

    def turn_left(self):
        super().turn_left()

    def turn_right(self):
        super().turn_right()