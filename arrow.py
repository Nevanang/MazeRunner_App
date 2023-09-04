import turtle,time

#Arrow class represents the turtle sprite that shows the movement
class Arrow(turtle.Turtle):
    def  __init__(self, start,Step,end,walls):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(0.5, 0.5, 1)
        self.color("red")
        self.goto(start)
        self.showturtle()
        self.stamp()
        self.speed('fast')
        self.Step=Step
        self.end = end
        self.walls = walls

    #Left Condition
    def faceLeft(self):
        if self.heading() ==0: #!Move Left condition
            x_walls = round(self.xcor(),0)
            y_walls = round(self.ycor(),0)
            #check if it is at the finish line
            if (x_walls, y_walls) in self.end:
                return False
            if (x_walls, y_walls+24) in self.walls:
                if (x_walls+24, y_walls) not in self.walls:
                    self.forward(24)
                    self.Step.add()
                    self.stamp() #mark the path taken
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
                self.Step.add()
                self.stamp() #mark the path taken
    #Right Condition
    def faceRight(self):
        if self.heading()== 180:
            x_walls = round(self.xcor(),0)
            y_walls = round(self.ycor(),0)
            #check if it is at the finish line
            if (x_walls, y_walls) in self.end:
                return False
            if (x_walls, y_walls-24) in self.walls: #check if there is any wall on the left
                if (x_walls-24, y_walls) not in self.walls:
                    self.forward(24)
                    self.Step.add()
                    self.stamp() #mark the path taken
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
                self.Step.add()
                self.stamp() #mark the path taken
    #Up Condition
    def faceUp(self):
        if self.heading()== 90:
            x_walls = round(self.xcor(),0)
            y_walls = round(self.ycor(),0)
            #check if it is at the finish line
            if (x_walls, y_walls) in self.end:
                return False
            if (x_walls-24, y_walls) in self.walls: #check if there is any wall on the left
                if (x_walls, y_walls+24) not in self.walls:
                    self.forward(24)
                    self.Step.add()
                    self.stamp() #mark the path taken

                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
                self.Step.add()
                self.stamp() #mark the path taken

    #Down Condition
    def faceDown(self):
        if self.heading()== 270:
            x_walls = round(self.xcor(),0)
            y_walls = round(self.ycor(),0)
            #check if it is at the finish line
            if (x_walls, y_walls) in self.end:
                return False
            if (x_walls+24, y_walls) in self.walls: #check if there is any wall on the left
                if (x_walls, y_walls-24) not in self.walls:
                    self.forward(24)
                    self.Step.add()
                    self.stamp() #mark the path taken
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)
                self.Step.add()
                self.stamp() #mark the path taken