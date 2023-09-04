import turtle

#Pen to make Step count
class Step(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.step=0
        self.goto(-300,-150)
        self.write(f'Steps: {self.step}',font=("Verdana",10, "normal"))

    # add steps for each algorithm
    def add(self):
        self.clear()
        self.step+=1
        self.goto(-300,-150)
        self.speed('fastest')
        self.write(f'Steps: {self.step}',font=("Verdana",10, "normal"))

    # generate informattion about algorithm
    def writeAlgo(self, algo):
        self.clear()
        self.goto(-300,-170)
        self.speed('fastest')
        self.write(f'Algorithm Switched to: {algo}',font=("Verdana",10, "normal"))
        self.goto(-60,-150)
        if algo == 'Breadth First Search':
            # Breadth first search
            self.write(
            """
            Breadth First Search (BFS) is an algorithm used for traversing or searching
            in a graph or tree data structure, where it visits all the vertices of a graph
            or all the nodes of a tree at the same level before moving on to the next level
            """,
             font=('Arial', 10, 'normal')
            )
        elif algo == 'Left Wall':
            # left hand
            self.write("""
            The Left Wall Algorithm works by always keeping one hand on the wall or boundary of the maze, 
            and using the hand to guide the direction of the traversal. 
            The algorithm is based on the principle that by keeping the left hand on the wall, 
            until it finds the endpoint
            """, font=('Arial',10,'normal')
            )
        elif algo == 'Depth First Search':
            self.write("""
            Depth First Search Algorithm
            """, font=('Arial',10,'normal')
        )

    # when endpoint blocked/no endpoint
    def notfound(self,):
        self.clear()
        self.goto(-50,-200)
        self.speed('fastest')
        self.write(f'Algorithm is unable to find a path',font=("Verdana",10, "normal"))

    # Record time taken for each algorithm to complete the maze
    def time_taken(self, starttime, endtime):
        self.goto(-150, -150)
        self.speed('fastest')
        self.write(f'Time Taken: {round((endtime-starttime),2)}', font=("Verdana", 10, "normal"))
    # clear steps
    def reset(self):
        self.step=0
        self.clear()