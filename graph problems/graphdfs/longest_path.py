"""
Given an integer matrix, return the length of the longest increasing path in the matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary. 
To make an increasing path, you can never move from one number to a number less-than-or-equal-to it.

Example:

Input:
[[9, 9, 4],
 [6, 6, 8],
 [2, 1, 1]]
Output: 4
Explanation: The longest path is [1, 2, 6, 9], which has length 4.

Hint: Can you find the longest increasing path starting at a specific cell?

longest path -> dfs 
memoization is important in the case where we have to find longest path in matrix 
memoization means keeping track of current progress with the path it's going on
"""
# using dfs approach and memoization

def longest_path(matrix):
  if not matrix:
    return []
  #check bounds 
  def inbounds(matrix, row , col):
    return row >=0 and row < len(matrix) and col >= 0 and col < len(matrix[row])
  memo = {} # (r,c)-pathvalue
  # dfs 
  def dfs(r,c,prev_value):
    #base case 
    if not inbounds(matrix,r,c)  or prev_value >= matrix[r][c]:
      return 0
    if (r,c) in memo:
      return memo[(r,c)]
    temp = matrix[r][c]
    #marking as visited 
    max_path_len = 1
    # print('memo is',memo)
    for dr , dc in [(1,0),(0,1),(-1,0),(0,-1)]:
      new_r = r + dr 
      new_c = c + dc
      print('pth is',max_path_len)
      max_path_len = max(max_path_len, 1+dfs(new_r, new_c, temp))
    memo[(r,c)] = max_path_len
    return max_path_len
  #starting points 
  max_length = 1 
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      # print('after calling' ,dfs(row,col,-1))
      max_length = max(max_length,dfs(row,col,-1))
      
  return max_length
matrix = [[9,9,4],
          [6,6,8],
          [2,1,1]]
print(longest_path(matrix))

    
        
                    