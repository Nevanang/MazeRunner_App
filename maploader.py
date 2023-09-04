import turtle, os

class MapLoader(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shapesize(3.5,3.5)
        self.shape("circle")
        self.color("black", "green")
        self.penup()
        self.goto(80, -170)
        self.stamp()
        self.goto(55, -180)
        self.write('Change Map\npress N',font=("Arial", 7, "bold"))

    def map_loader(self, pen,screen):
        filename=screen.textinput("Map Changer", "Enter name of file")
        if filename!=None and filename!='':
            if os.path.exists(filename)==False:
                pen.goto(55, -200)
                pen.write('Map not found',font=("Arial", 10, "bold"))
            else:
                pen.clear()
                pen.hideturtle()
                pen.shape("square")
                pen.shapesize(20/15)
                pen.color("black",'grey')
                pen.penup()
                pen.goto(-300,120)
                pen.write('PIZZA RUNNERS: Done by Nevan & Yu Yang DAAA/2B/01',font=("Verdana",12, "normal"))
                with open(filename) as f:
                    lines = f.readlines()
                return lines
        else:
            return