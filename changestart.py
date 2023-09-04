import turtle, math

class SetStart(turtle.Turtle):
    def  __init__(self, start,end, walls):
        turtle.Turtle.__init__(self)
        self.flag = True
        self.start = start
        self.end = end
        self.walls = walls
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(0.5, 0.5, 1)
        self.color("red")
        self.goto(start)
        self.showturtle()
        # self.stamp()
        self.speed(2)

    def move_forward(self):
        if self.flag:
            self.flag = False
            x, y = self.position()
            # Calculate the new position based on the heading and distance
            new_x = round(x + 24 * math.cos(math.radians(self.heading())), 0)
            new_y = round(y + 24 * math.sin(math.radians(self.heading())), 0)
            if (new_x,new_y) not in self.walls:
                self.forward(24)
            self.flag = True

    def turn_left(self):
        if self.flag:
            self.flag = False
            self.left(90)
            self.flag = True

    def turn_right(self):
        if self.flag:
            self.flag = False
            self.right(90)
            self.flag = True

    def move_back(self):
        if self.flag:
            self.flag = False
            x, y = self.position()
            # Calculate the new position based on the heading and distance
            new_x = round(x - 24 * math.cos(math.radians(self.heading())), 0)
            new_y = round(y - 24 * math.sin(math.radians(self.heading())), 0)
            if (new_x,new_y) not in self.walls:
                self.backward(24)
            self.flag = True

    def markLoc(self):
        if self.flag:
            self.flag = False
            if self.pos() == self.end:
                return
            self.start = self.pos()
            return self.start