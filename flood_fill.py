
'''
Problem : FloodFill
A grid contains '.' and 'X' starting from point (0,0) Fill the grid with '0'

'.' is a free space, meaning it can be changed to an '0'
'X' is an obstacle. You cannot go past an obstacle, or change an obstacle to an '0'
From a position you can move in the cardinal directions

Input :  [['.','X','.','.','.'],
          ['.','X','.','.','.'],
          ['.','.','X','.','.']]

Expected : [['0','X','.','.','.'],
          ['0','X','.','.','.'],
          ['0','0','X','.','.']]


'''


def floodfill(grids):
  #edge case 
  if not grids:
    return grids 
  #checking bounds 
  def inbounds(grids,r,c):
    return r>= 0 and r < len(grids) and c >= 0 and  c < len(grids[r])
  def helper(grids,r,c):
    # base cases 
    if not inbounds(grids,r,c) or grids[r][c]=='0' or grids[r][c]=='X':
      return 
    #mark visited 

    grids[r][c]='0'
    # process the neighbors
    for dr , dc in [(1,0),(0,1),(-1,0),(0,-1)]:
      new_r = r + dr 
      new_c = c + dc 
      helper(grids,new_r,new_c)
 #starting nodes 
  helper(grids,0,0)
  return grids # inplace replacing 

grids = [['.','X','.','.','.'],
          ['.','X','.','.','.'],
          ['.','.','X','.','.']]
print(floodfill(grids))