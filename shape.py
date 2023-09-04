import turtle

#Breadth First Search
#color all roads as yellow dots
class Shape(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shapesize(20*0.5/15*0.5)
        self.hideturtle()
        self.shape('turtle')
        self.color("blue")
        self.penup()
        self.speed('fastest')