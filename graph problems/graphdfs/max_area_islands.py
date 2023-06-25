'''
Problem : You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

'''
#dfs problem 

def max_area_island(grid):
    # edge case 
    if not grid:
        return 0
    # check bounds 
    def inbounds(grid,r,c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])
    #dfs 
    def dfs(grid,r,c):
        #base case 
        if not inbounds(grid,r,c) or grid[r][c]==0:
            return 0
        # initial area 
        area = 1
        # mark visited 
        grid[r][c] = 0
        #process neighbors 
        for dr , dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            new_r = r + dr 
            new_c = c + dc 
            area += dfs(grid,new_r,new_c)

        return area 
    #starting points 
    max_area = 0 
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]==1:
                max_area = max(dfs(grid,row,col),max_area)
    return max_area 

grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(max_area_island(grid))
# Time Complexity: O(n*m)
# Space Complexity: O(n*m)