# MazeRunner_App
Using Algorithms to Solve Mazes
Scenario: A startup company delivering pizzas wants to navigate their drones with optimal efficiency in a city map, made up of:

X:  Building (drone can’t go here)
.:  Road ( drone can fly here)
s:  The start location of the drone
e: The pizza delivery location

Create a Maze-Running App that can find possible ways to traverse a city to a specified destination
Includes:

Map,
Input Map file,
Algorithm Selector

Done on Python with @yuyang-khor, Press Tab to start

Left Hand Algorithm
In our turtle program, we applied the wall follower algorithm using the left hand rule, which is based on the simple logic of movements whereby it follows along the left side of the enclosure wall all the way to the exit. 

Breadth First Search Algorithm
Breadth First Search is a tree traversal and search algorithm which begins at a tree root, explores its neighbours or nodes that are nearest to it, before moving to its subsequent neighbouring node and exploring its neighbours. This is called depth, where there are layers of depth based on the distance a node is from the tree root.
In the case of our Pizza Runner, the tree root would be the start square block and the nodes are the road square blocks.

Depth First Search Algorithm
Compared to Breadth First Search, instead of adding all nearest neighbors and exploring all possible routes (and completing layer by layer), it explores routes one by one  until it has nowhere else to explore. It explores as far as possible along each branch before backtracking recursively


