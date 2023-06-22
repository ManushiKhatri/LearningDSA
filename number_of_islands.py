'''
Problems : Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


'''
#dfs approach 
def number_of_islands(grid): 
    if not grid:
        return 0
    #check bounds 
    def inbounds(grid,r,c):
        return r >=0 and r < len(grid) and c >= 0 and c < len(grid[r])
    #dfs 
    def dfs(r,c):
        #base case 
        if not inbounds(grid,r,c) or grid[r][c]=='0':
            return 
        #mark visited 
        grid[r][c] = '0'
        #check neighbors
        for dr , dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            new_r = r + dr 
            new_c = c + dc 
            dfs(new_r,new_c)
    #starting co-ordinates  
    total_area = 0 
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1':
                total_area += 1
                dfs(row,col)
    return total_area


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(number_of_islands(grid))