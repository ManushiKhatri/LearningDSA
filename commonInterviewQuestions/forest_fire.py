'''
Forest Fires
Difficulty: Medium



Background
Forest fires are really dangerous, and can be started by even the smallest flame. Spreading from tree to tree, fires can engulf an entire forest in a matter of weeks. These fires cannot cross a body of water, and are the only way to stop these aggressive fires (temporarily, until they evaporate!). Given a map of a forest with locations of where a fire, water, trees, determine whether or not the fire can destroy the entire forest and how long it will take.

Problem
The input will contain a 10x10 map. On this map you will see the following symbols: • . - blank space, which is fire neutral (ex. sand or rock)
• T - a tree
• F - a tree on fire
• W - water

FIRES only spread from existing fire to adjacent trees, in 4 directions (so not diagonally). It takes 1 unit of time for the fire to spread from one location to the next in the 4 available directions. Assume that once a square become 'F', it stays that way until the end of the test case. The fire spreads in all 4 directions at the same time.

If TREES have water in at least one of their 4 directions, then they cannot catch fire until their water is evaporated.

WATER becomes evaporated if fire touches it from ANY direction (take that Pokemon physics, fire beats water in MPC!). So 'W' becomes '.' NEXT TIME UNIT if F is in at least one of its 8 surrounding squares. When water is evaporated, it can no longer protect the trees from fire. If fire meets a tree (F meets T) then the tree becomes a fire as well.

Assume that all of these mentioned events are all updated at the same unit of time. The output will be one integer: the time it takes for the fire to capture the entire forest. If some piece of the forest survives indefinately, output -1.

Input
One spruced up forest (hehe). A forest consists of 10 lines. Each line consists of spaced characters that may be '.', '-', 'F', 'W' or 'T'.

Output
An integer representing the time for the forest to burn down. -1 indicates that the forest does not burn down.

Input Test Case 1

..........
..........
..........
..........
..TTWTTT..
..F.......
..........
..........
..........
..........

Output Test Case 1

-1
The water evapotates and turns into '.', but the fire can't reach all of the forest!

Input Test Case 2

..........
..........
...TTT....
...TWTTT..
...F......
..........
..........
..........
..........
..........

Output Test Case 2

8
In the first unit of time, the water evaporates and the next 7 units of time the fire takes out the forest.



'''
# similar to the rotten orange problem 

from collections import deque 
def total_time(matrix):
    total_trees = 0
    q = deque()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'T':
                total_trees += 1
            elif matrix[row][col] == 'F':
                q.append((row, col))

    total_time = 0 
    q.append(None)

    while q:
        node = q.popleft()
        if node is None:
            if q:
                q.append(None)
                total_time += 1
        else:
            r, c = node 
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r = r + dr 
                new_c = c + dc

                if inbounds(matrix, new_r, new_c) and matrix[new_r][new_c] != 'F' and matrix[new_r][new_c] != '.':
                    if matrix[new_r][new_c] == 'T':
                        q.append((new_r, new_c))
                        matrix[new_r][new_c] = 'F'
                        total_trees -= 1
                    elif matrix[new_r][new_c] == 'W':
                        matrix[new_r][new_c] = '.'  # Fixed the evaporation step
                        total_time += 1
    return total_time if total_trees == 0 else -1
                    
def inbounds(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[row])

forest = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'T', 'T', 'T', '.', '.', '.', '.'],
    ['.', '.', '.', 'T', 'W', 'T', 'T', 'T', '.', '.'],
    ['.', '.', '.', 'F', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
print(total_time(forest))

forest1=[
 ['F', 'T', 'F', 'T', 'T', 'T', '.', '.', '.', '.'],
 ['.', '.', '.', 'W', 'W', 'W', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
print(total_time(forest1))

forest2=[
 ['.', '.', '.', 'F', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'T', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'T', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'T', 'W', '.', '.', '.', '.', '.'],
 ['.', '.', '.', 'T', 'T', 'T', '.', '.', '.', '.'],
 ['.', '.', '.', '.', 'W', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
print(total_time(forest2))

