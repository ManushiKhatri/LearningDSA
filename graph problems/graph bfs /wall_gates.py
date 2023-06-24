'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

MODIFY THE LIST IN-PLACE!!!!!!!!!!!

Examples
Repl.it logo
Input: rooms = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

'''
def walls_gates(grids):

  def inbounds(r, c, grids):
    return r >= 0 and r < len(grids) and c >= 0 and c < len(grids[r])

  # if it is a graph? -> yes
  #1. base case
  if not grids:
    return grids
  #2.initialize tracking variables
  q, visited, distance = deque(), set(), 0
  #intaking nodes
  for row in range(len(grids)):
    for col in range(len(grids[row])):
      if grids[row][col] == 0:
        q.append((row, col))
        visited.add((row, col))

  #intaking nodes
  #process q
  while q:
    r, c = q.popleft()
    # update the distance for current visit
    distance = grids[r][c]
    #visinting the neighbours
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      new_r = r + dr
      new_c = c + dc
      if inbounds(new_r, new_c, grids) and (
          new_r, new_c) not in visited and grids[new_r][new_c] == 2147483647:
        # updating the distance
        grids[new_r][new_c] = distance + 1
        visited.add((new_r, new_c))
        q.append((new_r, new_c))
  return grids


rooms = [[2147483647, 0, -1, 2147483647],
         [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
print(walls_gates(rooms))
