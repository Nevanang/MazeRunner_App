import turtle

#Turtle Class
class Pen(turtle.Turtle):
    def  __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(20/15)
        self.color("black",'grey')
        self.penup()
        self.goto(-300,120)
        self.write('PIZZA RUNNERS: Done by Nevan & Yu Yang DAAA/2B/01',
        font=("Verdana",12, "bold", 'underline'))
        self.speed(10)