'''

There is a rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
 The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. 
 You are given a grid of matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a list of all of the grid coordinates in the form (r, c) where rain water can flow from that cell to both the Pacific and Atlantic oceans.

input : 
Input:
[[1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]]
#pacific ocean : row - 1,col-1 , out of bound
#atlantic ocean , row + 1 , col + 1
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans, we just care if there is *any* path.

'''
# this problem requires strong understandig of the problem
from collections import deque 

def water_overflow(grid):
    #edge case 
    if not grid:
        return []
    #check bounds 
    def inbounds(grid,r,c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])
    #dfs 

    def bfs(grid, stack):
       explored = set()
       while stack: 
              v = stack.pop()
              # print('exploreing is ',explored)
              if v not in explored:
                explored.add(v)
              #process neighbors 
                r, c= v 
                for dr , dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                  new_r = r + dr 
                  new_c = c + dc 
                  if inbounds(grid, new_r, new_c) and grid[new_r][new_c] >= grid[r][c]:
                         stack.append((new_r,new_c))
       return explored
    #storing pacific top level and atlantic low level in stack 
    pacific_ocean = deque()
    atlantic_ocean = deque()
    for row in range(len(grid)):
           pacific_ocean.append((row,0))
           atlantic_ocean.append((row,len(grid[row])-1))
    for col in range(len(grid[0])):
           pacific_ocean.append((0,col))
           atlantic_ocean.append((len(grid)-1,col))
#     print('atlantic ',atlantic_ocean)
#     print('pacific is ',pacific_ocean)
    pacific_overflow = bfs(grid,pacific_ocean)
    atlantic_overflow = bfs(grid,atlantic_ocean)
    return list(pacific_overflow & atlantic_overflow) # & works as intersection between pacific and intersection , it's a set functionality 
grid = [[1,2,2,3,5],
       [3,2,3,4,4],
       [2,4,5,3,1],
       [6,7,1,4,5],
       [5,1,1,2,4]]
print(water_overflow(grid))
