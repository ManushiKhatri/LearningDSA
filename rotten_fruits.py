'''

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.


'''

"""
what do we need ??

count of fresh orange ?
rotten orange ??
is it bfs problem or dfs ??
q
"""
from collections import deque 

def rotten_oranges(grid):
    # edge case 
    if not grid:
        return 0

    # check in bound 
    def inbounds(grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])
    
    # initiate variables 
    q = deque()
    fresh_orange, time = 0, 0
    
    # append the rotten orange in queue
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                fresh_orange += 1
            if grid[i][j] == 2:
                q.append((i, j))

    if not q:  # If there's no rotten orange at the beginning.
        return -1 if fresh_orange > 0 else 0  # If there are fresh oranges, return -1. Else, return 0.

    # append the None to mark as level
    q.append(None)

    # process the queue 
    while q:
        node = q.popleft()

        if node is None:
            if q:  # if there are still items to process
                q.append(None)
                time += 1
        else:
            r, c = node 
            # traverse through all the directions 
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                new_r = r + dr
                new_c = c + dc
                if inbounds(grid, new_r, new_c) and grid[new_r][new_c] == 1:
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = 2
                    fresh_orange -= 1

    return time if fresh_orange == 0 else -1

grid = [[0,2]]
print("Time taken to rot: ", rotten_oranges(grid))  # expected -> 0      
grid = [[2,1,1],[1,1,0],[0,1,1]]
print("Time taken to rot : ",rotten_oranges(grid)) # expected -> 4
grid1=[[2,1,1],[0,1,1],[1,0,1]]
print("Time taken to rot : ",rotten_oranges(grid1))#expected -1

        
