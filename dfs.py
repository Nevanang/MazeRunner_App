import turtle

# Depth First Search Algorithm
class DFS(turtle.Turtle):
    def __init__(self,stack,road,start,end,Step,Shape,Arrow):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(0.5, 0.5, 1)
        self.color("red")
        self.next_cell=stack #list of cells to go to next
        self.road=road #positions in turtle(x,y)
        self.start=start
        self.Step = Step
        self.shape = Shape
        self.arrow = Arrow
        self.end=end
        self.visited=set()#set
        self.solution={}
        #Road square block is added to a stack and the function continues to visit the neighbors of the Road square block until a it has no more neighbors to visit. 
        #Once all neighbors of that certain block have been visited, the function backtracks to the previous node by popping the last node 
        # from the stack and visiting its neighbors. This continues until the goal is found or there are no more nodes to visit.
    def graph_create(self):
        x,y=self.start[0],self.start[1]
        self.next_cell.push((x, y))   # add the x and y position to the stack, meant to
        self.solution[x,y] = x,y # add x and y to the solution dictionary

        while self.next_cell.size() > 0:                           # loop until the frontier list is empty
            current=(x,y)
            if(x - 24, y) in self.road and (x - 24, y) not in self.visited:  # check left

                cellleft = (x - 24, y)
                self.solution[cellleft] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
                self.shape.goto(cellleft)
                self.shape.stamp()
                self.next_cell.push(cellleft)  # add cellleft to the cell next list

            if (x, y - 24) in self.road and (x, y - 24) not in self.visited:  # check down
                celldown = (x, y - 24)
                self.solution[celldown] = x, y
                self.shape.goto(celldown)
                self.shape.stamp()
                self.next_cell.push(celldown)

            if(x + 24, y) in self.road and (x + 24, y) not in self.visited:   # check right
                cellright = (x + 24, y)
                self.solution[cellright] = x, y 
                self.shape.goto(cellright)
                self.shape.stamp()
                self.next_cell.push(cellright)

            if(x, y + 24) in self.road and (x, y + 24) not in self.visited:  # check up
                cellup = (x, y + 24)
                self.solution[cellup] = x, y
                self.shape.goto(cellup)
                self.shape.stamp()
                self.next_cell.push(cellup)

            #current cell becomes last entry in frontier list
            x, y = self.next_cell.pop()
            # print(x)        
            self.visited.add(current) # add current cell to visited list
            self.shape.goto(x,y) # green turtle goto x and y position
            self.shape.stamp() # stamp a copy of the green turtle on the maze

    def backRoute(self,end_x,end_y):
        self.arrow.goto(end_x, end_y)
        self.arrow.stamp()
        if ((end_x,end_y)) not in self.solution:
            self.Step.notfound()
        #if end coord not in dictionary 
        else:
            if (end_x, end_y) == (self.start[0], self.start[1]):
                return
            else:
                self.Step.add()
                next_x, next_y = self.solution[end_x, end_y]
                self.backRoute(next_x, next_y)