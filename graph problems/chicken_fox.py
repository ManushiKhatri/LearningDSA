"""
Try this one if you liked the Die Hard problem.

There are 3 chickens, 3 foxes, and 1 boat on one side of the river, and everyone wants to get to the other side of the river. Rules:

- The boat can hold a maximum of two animals at a time
- If there are ever more foxes than chickens on either side of the river, those chickens get eaten. You lose.
- At least one animal must be on the boat in order to row it (the boat can't row itself to the other shore). These animals have hands and are able to operate oars.

Return the shortest path (the solution with the fewest number of boat moves) that gets everyone safely from one side of the river to the other. I won't tell you the solution - you have to find it!

Remember that to solve a BFS problem like this, you need to answer these four questions:

- How are you representing your nodes?
- What are the neighbors of a node?
- What is the start node?
- What is the destination node?

**Hint:** If you know what's on one side of the river, you know (by subtraction) what's on the other side of the river. Does your node actually need to hold information about both sides? The smallest node representation I can think of needs only 3 values.


"""

from collections import deque


def is_valid(node):
  chicken_0, fox_0 = node[0], node[1]
  chicken_1, fox_1 = 3 - node[0], 3 - node[1]
  return (chicken_0 >= fox_0 or chicken_0 == 0) and (chicken_1 >= fox_1 or chicken_1 == 0) and \
      chicken_0 >= 0 and chicken_1 >= 0 and fox_0 >= 0 and fox_1 >= 0


def get_neighbors(node):
  neighbors = []
  chicken_0, fox_0, boat = node
  if boat == 0:
    neighbors.append((chicken_0 - 2, fox_0, 1))
    neighbors.append((chicken_0 - 1, fox_0, 1))
    neighbors.append((chicken_0 - 1, fox_0 - 1, 1))
    neighbors.append((chicken_0, fox_0 - 1, 1))
    neighbors.append((chicken_0, fox_0 - 2, 1))
  else:
    neighbors.append((chicken_0 + 2, fox_0, 0))
    neighbors.append((chicken_0 + 1, fox_0, 0))
    neighbors.append((chicken_0 + 1, fox_0 + 1, 0))
    neighbors.append((chicken_0, fox_0 + 1, 0))
    neighbors.append((chicken_0, fox_0 + 2, 0))
  return [neighbor for neighbor in neighbors if is_valid(neighbor)]


def retrace_steps(dst, parents):
  if dst not in parents:
    return None

  path = []
  curr = dst
  while curr:
    path.append(curr)
    curr = parents[curr]
  path.reverse()
  return path


def chicken_fox():
  q = deque()
  parent = {}

  src, dst = (3, 3, 0), (0, 0, 1)
  parent[src] = None
  q.append(src)
  while q:
    v = q.popleft()
    if v == dst:
      return retrace_steps(dst, parent)
      break
    for w in get_neighbors(v):
      if w not in parent:
        parent[w] = v
        q.append(w)

  return retrace_steps(dst, parent)


print('\nChicken Fox\n')

print(chicken_fox())