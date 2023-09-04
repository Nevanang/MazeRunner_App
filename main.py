# import networkx
import turtle, sys, time, functools, os
from changestart import SetStart
from race import OneVsOne
from hash import HashTable
from step import Step
from shape import Shape
from bfs import BFS
from pen import Pen
from arrow import Arrow
from queue import Queue
from dfs import DFS
from stack import Stack
from maploader import MapLoader

#Create the canvas
screen=turtle.Screen()
screen.title('Pizza Delivery')
screen.bgcolor('white')
screen.setup(width=700,height=500)

#MAP setup function
def setup_maze(level,road,walls,end,start):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -300 + (x *24)
            screen_y = 100 - (y * 24)

            if character =="X": #Buildings
                pen.goto(screen_x, screen_y)
                pen.color('black','grey')
                pen.stamp() #draw the square
                walls.append((screen_x,screen_y))
            elif character == ".": #Road
                pen.goto(screen_x,screen_y)
                road.append(pen.pos()) #append the position to list
                pen.color('black','white')
                pen.stamp() #draw the square
            elif character == "s": #Start Point
                pen.goto(screen_x,screen_y)
                # arrow.goto(screen_x,screen_y)
                start.append(pen.pos())
                pen.color('black','lightgreen')
                pen.stamp() #draw the square
            elif character == "e": #End Point
                pen.goto(screen_x,screen_y)
                end.append(pen.pos())
                road.append(pen.pos())#for bfs
                pen.color('black','cyan')
                pen.stamp() #draw the square

active_func = 'left' #global variable

# Left Wall follower function
def left_path():
    while True: # Loop the action movement until it finds the end point and return False
        if arrow.faceLeft()== False or arrow.faceRight()==False \
        or arrow.faceUp()==False or arrow.faceDown()==False:
            return

# toggle between three algorithms using tab
def toggle_function():
    global active_func
    if active_func =='left':
        active_func = 'short'
        algo_step.writeAlgo('Breadth First Search')

    elif active_func == 'dfs':
        active_func = 'left'
        algo_step.writeAlgo('Left Wall')

    elif active_func == 'short':
        active_func = 'dfs'
        algo_step.writeAlgo('Depth First Search')

flag = True #global flag

# Run the algorithms with the toggled algorithm
def run_algorithm():
    global active_func, flag, flag_but
    if flag and flag_but and mapflag:
        flag = False
        arrow.clear()
        shape.clear()
        arrow.hideturtle()
        arrow.goto(start[0])
        arrow.showturtle()
        steps.reset()

        if active_func == 'left': # Left hand Algorithm
            starttime = time.perf_counter()
            left_path()
            endtime = time.perf_counter()
            steps.time_taken(starttime, endtime) # calculate timetaken
            screen.title(f"Pizza Delivery Current Algorithm: Left Hand, Steps Taken: {arrow.Step.step}")
            flag = True

        elif active_func == 'short' : # Breadth First Search Algorithm
            starttime = time.perf_counter()
            bfs=BFS(queue,road,start[0],end[0],steps,arrow,shape)
            bfs.graph_create()
            bfs.backRoute(end[0][0],end[0][1])
            endtime = time.perf_counter()
            steps.time_taken(starttime, endtime) # calculate timetaken
            screen.title(f"Pizza Delivery Current Algorithm: Breadth First Search, Steps Taken: {bfs.Step.step}")
            flag = True

        elif active_func == 'dfs': # Depth First Search Algorithm
            starttime = time.perf_counter() # track start time
            dfs=DFS(stack,road,start[0],end[0],steps,shape,arrow)
            dfs.graph_create()
            dfs.backRoute(end[0][0],end[0][1])
            endtime = time.perf_counter()
            steps.time_taken(starttime, endtime) # calculate timetaken
            screen.title(f"Pizza Delivery Current Algorithm: Depth First Search, Steps Taken: {dfs.Step.step}")
            flag = True

flag_but = True
mapflag=True

# control turtle sprite
def controlStart(x,y,but):
    global flag_but
    screen.title('Pizza Delivery')
    if flag_but and flag and mapflag:

        # inner function to mark the new start point
        def newStart():
            global flag_but
            nonlocal setS

            # Disable onkeypress event handler
            screen.onkeypress(None, "m")
            pen.goto(start[0])
            pen.color('black','white') # change the original start point to part of road
            road.append(start[0])
            pen.stamp() #draw the square
            temp = setS.markLoc()
            if temp is None: # when user set start at end
                arrow.showturtle()
                # reset flag
                flag_but = True
                # reset button
                but.clear()
                start_create_button()
            start[0] = round(temp[0],0), round(temp[1], 0)
            setS.hideturtle()
            arrow.goto(start[0]) # change the set point to start point
            pen.goto(start[0])
            pen.color('black','lightgreen')
            pen.stamp() #draw the square
            arrow.showturtle()
            # reset flag
            flag_but = True
            # reset button
            but.clear()
            start_create_button()
        flag_but = False
        arrow.clear()
        arrow.hideturtle()
        shape.clear()
        # enable turtle to show that button is unavailable now
        but.color("black", "red")
        but.goto(100, 70)
        but.stamp()
        but.goto(88, 65)
        but.write('Wait!',font=("Arial", 7, "bold"))
        setS = SetStart(start[0],end[0],walls) # let user control sprite
        screen.onkeypress(setS.move_forward,'w') # forward key
        screen.onkeypress(setS.turn_left,'a') # turn left key
        screen.onkeypress(setS.move_back,'s') # move backward key
        screen.onkeypress(setS.turn_right,'d') #turn right key
        screen.onkeypress(newStart,'m') # mark current coord as start point
        screen.listen() #wait for keyboard input

# Button Function
def start_create_button():
    button = turtle.Turtle()
    button.hideturtle()
    button.shape("circle")
    button.color("black", "lightgreen")
    button.shapesize(1.5, 1.5)
    button.penup()
    button.goto(100, 70)
    button.stamp()
    button.goto(88, 65)
    button.write('Click!',font=("Arial", 7, "bold"))

    text = turtle.Turtle()
    text.hideturtle()
    text.color('black')
    text.penup()
    text.goto(40, 90)
    # text.pendown()
    text.write('Change Start Position', font=("Arial", 10, "bold", 'underline'))
    # text.goto(100,0)
    screen.onscreenclick(lambda x, y: controlStart(x, y, button) if button.distance(x, y) < 30 else None)

# race counter
race_counter = 1

# Race Function
def raceF(x,y,but,result):
    # Flags to ensure no other functions interrupts it
    global flag_but
    screen.title('Pizza Delivery')
    if flag_but and flag and mapflag:

        # Inner Function to check if it is at the end point
        def ifEndF():
            global flag_but, race_counter
            nonlocal result
            # check if it reaches the end point
            if one_one.move_forward():
                print('Reached the end')
                time2 = time.time() # get end time
                time_taken = round((time2 - time1), 2) # calculate time taken
                result[user_name] = time_taken # store into hashtable
                but.goto(-250,200)
                but.write(f'{user_name}, You took {time_taken} seconds',font=("Arial", 12, "normal"))
                if race_counter != 2: # run function again for second player
                    race_counter += 1 #add counter to track current player
                    one_one.hideturtle()
                    one_one.clear()
                    time.sleep(2) #delay
                    # undo two steps for button to revert for second player
                    but.undo()
                    but.undo()
                    but.undo()
                    flag_but = True
                    raceF(x,y,but,result)
                elif race_counter == 2:
                    one_one.hideturtle()
                    one_one.clear()
                    time.sleep(2)
                    but.undo() #undo to last action

                    # check if both player result are the same
                    if result.buckets[0] == result.buckets[1]:
                        but.write(f'Wow! Both of you have the same result of {result.buckets[0]}. TIE',font=("Arial", 10, "normal"))
                        time.sleep(2)
                        but.clear()
                        flag_but = True
                        arrow.showturtle()
                        race_counter = 1 # reset race counter for next player
                        best = 0
                        race_button() # rerun function to reset button
                        return
                    best = min(result.buckets) # find minimum time for best player
                    # Loop to reveal results of the race maze
                    if result[result.keys[0]] == best:
                        but.write(f'Congrats to {result.keys[0]}, with best timing of {result[result.keys[0]]} seconds',font=("Arial", 10, "normal"))
                        but.goto(-250,180)
                        but.write(f"Better Luck to {result.keys[1]}, with {result[result.keys[1]]} seconds",font=("Arial", 10, "normal"))
                    else:
                        but.write(f'Congrats to {result.keys[1]}, with best timing of {result[result.keys[1]]} seconds',font=("Arial", 10, "normal"))
                        but.goto(-250,180)
                        but.write(f"Better Luck to {result.keys[0]}, with {result[result.keys[0]]} seconds",font=("Arial", 10, "normal"))

                    time.sleep(2)
                    but.clear() #clear button
                    flag_but = True
                    arrow.showturtle()
                    screen.onkeypress(None, 'w') # disable keypress
                    race_counter = 1
                    best = 0
                    race_button() #re run function to reset button
                    return
        # Obtain user name for better tracking
        user_name = ""
        while user_name == '':
            user_name = screen.textinput("Input", "Enter your username:")
            if not user_name or race_counter ==1 and user_name =="":
                return
        flag_but = False
        # clear the turtle on the map for the race to occur
        arrow.clear()
        arrow.hideturtle()
        shape.clear()
        # algo_step.clear()
        # steps.clear()
        # enable turtle to show that button is unavailable now
        but.color("black", "red")
        but.goto(100, -40)
        but.stamp()
        but.goto(88, -45)
        but.write('Wait!',font=("Arial", 7, "bold"))
        one_one = OneVsOne(start[0],end[0],walls) # initialize class for race
        # countdown timer before user can start controlling
        but.goto(100,200)
        for i in range(3, 0, -1):
            but.write(f'Ready in {i}',font=("Arial", 10, "bold"))
            time.sleep(1)
            but.undo()
        # but.undo()
        but.write('GO!',font=("Arial", 10, "bold"))
        time1 = time.time()
        screen.onkeypress(ifEndF, 'w') # forward key
        screen.onkeypress(one_one.turn_left,'a') # turn left key
        # screen.onkeypress(ifEndB,'s') # move backward key
        screen.onkeypress(one_one.turn_right,'d')  #turn right key
        screen.listen() #wait for keyboard input

# Button for OnevsOne competition
def race_button():
    # initialize hashtable
    race_history = HashTable(size=2)
    button = turtle.Turtle()
    button.hideturtle()
    button.shape("circle")
    button.color("black", "orange")
    button.shapesize(1.8, 1.8)
    button.penup()
    button.goto(100, -40)
    button.stamp()
    button.goto(86, -45)
    button.write('Press R',font=("Arial", 7, "bold"))

    text = turtle.Turtle()
    text.hideturtle()
    text.color('black')
    text.penup()
    text.goto(60, -20)
    # text.pendown()
    text.write('Start 1v1 race', font=("Arial", 10, "bold", 'underline'))
    # text.goto(100,0)
    screen.onkeypress(functools.partial(raceF,x=0,y=0,but=button,result=race_history),'r')

# function to change map and reload the coordinates of properties in maze
def ChangeMap():
    global road, walls, end, start,arrow, mapflag
    if flag and flag_but and mapflag:
        mapflag = False
        lines = maploader.map_loader(pen,screen)
        road = []
        walls = []
        end = []
        start = []
        setup_maze(lines,road,walls,end,start)
        arrow.clear()
        arrow.hideturtle()
        arrow = Arrow(start[0],steps,end,walls)
        mapflag = True

#Main Program
pen=Pen()
shape=Shape()
road=[]
walls=[]
end=[] # start and end is in tuple, [(x,y)]
start=[]
queue=Queue()
stack=Stack()

#retrieve txt filename from command line
filename = sys.argv[-1] #last argument

#check if the file opened is txt
if filename[-4:]!=".txt":
    raise Exception('Sorry, the file type specified was not correct...Please Try Again')
try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError: #if filename is not correct
    print('filename specified does not exists...Please Try Again')

# Set up the Maze
setup_maze(lines,road,walls,end,start)
steps=Step()
algo_step=Step()
algo_step.writeAlgo('Left Wall')
arrow=Arrow(start[0],steps,end,walls)
maploader = MapLoader()
start_create_button() #Create button for switching start point
race_button() #Create button for starting the race

# Key Binds
screen.listen() #wait for keyboard input
screen.onkeypress(toggle_function,'Tab') #trigger switch function algo
screen.onkeypress(run_algorithm,'space') #trigger run function run algo
screen.onkeypress(ChangeMap,'n') #map changer

while True:
    screen.update()