import turtle

# Breadth First Search Class
class BFS(turtle.Turtle):
    def __init__(self,queue,road,start,end, Step,arrow,shape):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.shape("turtle")
        self.shapesize(0.5, 0.5, 1)
        self.color("red")
        self.queue=queue #the graph
        self.road=road #positions in turtle(x,y)
        self.start=start
        self.Step = Step
        self.end=end
        self.visited=set()#set
        self.solution={}
        self.arrow = arrow
        self.shape = shape

    def graph_create(self): #start x start y
        self.endfound=False
        self.queue.enqueue((round(self.start[0],0),round(self.start[1],0)))
        self.solution[round(self.start[0],0),round(self.start[1],0)]=round(self.start[0],0),round(self.start[1],0)

        while self.queue.size()>0:
            self.x,self.y=self.queue.get()
            # print(f'{self.x} X IS HERE')
            # print(f'{self.y} y is here')
            self.queue.dequeue() # Pop first element of Queue, Get popped element And begin traversal of A adjacent vertex
            if self.endfound==True:
                return
            if(self.x - 24, self.y) in self.road and (self.x - 24, self.y) not in self.visited:  # check the cell on the left
                cell = (self.x - 24, self.y)
                self.solution[cell] = self.x, self.y    # backtracking routine [cell] is the previous cell. x, y is the current cell
                self.queue.enqueue(cell)   # add cell to deque
                self.visited.add((self.x-24, self.y))  # add cell to visited list
                self.checkend((self.x-24, self.y))

            if (self.x, self.y - 24) in self.road and (self.x, self.y - 24) not in self.visited:  # check the cell down
                cell = (self.x, self.y - 24)
                self.solution[cell] = self.x, self.y
                #blue.goto(cell)
                #blue.stamp()
                self.queue.enqueue(cell)
                self.visited.add((self.x, self.y - 24))
                self.checkend((self.x, self.y - 24))
                # print(self.solution)

            if(self.x + 24, self.y) in self.road and (self.x + 24, self.y) not in self.visited:   # check the cell on the right
                cell = (self.x + 24, self.y)
                self.solution[cell] = self.x, self.y
                #blue.goto(cell)
                #blue.stamp()
                self.queue.enqueue(cell)
                self.visited.add((self.x +24, self.y))
                self.checkend((self.x +24, self.y))

            if(self.x, self.y + 24) in self.road and (self.x, self.y + 24) not in self.visited:  # check the cell up
                cell = (self.x, self.y + 24)
                self.solution[cell] = self.x, self.y
                #blue.goto(cell)
                #blue.stamp()
                self.queue.enqueue(cell)
                self.visited.add((self.x, self.y + 24))
                self.checkend((self.x, self.y + 24))
            #need to add end inside
            self.shape.goto(self.x,self.y)
            self.shape.stamp()
    def checkend(self,coordinates):
        if coordinates==self.end:
            self.endfound=True

    def backRoute(self,end_x,end_y):
        self.arrow.goto(end_x, end_y)
        # print(self.solution)
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