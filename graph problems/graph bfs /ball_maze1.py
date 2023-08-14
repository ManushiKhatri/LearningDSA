"""
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through the empty spaces by moving up, down, left or right, one space at a time. 
It can't move through walls or out of bounds.

Given the maze, the ball's start position and the destination, where start = (startrow, startcol) and destination = (destinationrow, destinationcol), return the shortest path the ball can take from start to destination.


Input: maze = [
  [0,0,1,0,0],
  [0,0,0,0,0],
  [0,0,0,1,0],
  [1,1,0,1,1],
  [0,0,0,0,0]
], start = (0,4), destination = (4,4)
Output: [(0, 4), (0, 3), (1, 3), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
(It's also possible for the first two moves to be different and still have a shortest path.)


"""
# bfs approach 
from collections import deque
def ball_maze(maze,start,dest):
    #edge case 
    if not maze:
        return [] # output in list so 
    # check bounds 
    def inbounds(maze,r,c):
        return r >=0 and r < len(maze) and c >= 0 and c < len(maze[r])
    # create a queue
    q = deque()
    # print(" q is",q)
    #tracking variables
    final_output ,visited = [], set()
    # append the starting node in q 
    q.append(start)    
    while q:
        # get the node
        node = q.popleft()
       
        #check if we reached our goal 
        if node == dest:
            return final_output
        #process the neighbors
        row , col = node 
        for dr , dc in [(1,0),(0,-1),(0,1),(-1,0)]:
            new_r = dr + row
            new_c = dc + col
            if inbounds(maze,new_r,new_c) and maze[new_r][new_c]!=1 and (new_r,new_c) not in visited:
                final_output.append((new_r,new_c))
                q.append((new_r,new_c))
                visited.add((new_r,new_c))
    return final_output

maze = [
  [0,0,1,0,0],
  [0,0,0,0,0],
  [0,0,0,1,0],
  [1,1,0,1,1],
  [0,0,0,0,0]
]
start = (0,4)
destination = (4,4)
print("ball maze is")
print(len(ball_maze(maze,start,destination)))
