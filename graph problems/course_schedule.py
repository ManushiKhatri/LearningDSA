'''

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

'''

# using dfs --> kind of topological sort approach 
from collections import defaultdict
def course_schedule(numcourses,preq):
    #tracking variables 
    # graph given ?
    graph = defaultdict(list)
    for crs,pre in preq:
        graph[crs].append(pre)
    visited,fully_explored = set(),set()
    def dfs(course,visited,fully_explored):
        #base cases 
        if course in visited:
            return False  # detected cycles already visited 
        if course in fully_explored:
            return True 
        if course not in graph:#no prerequisties needed 
            return True 
        visited.add(course)
        for neighbor in graph[course]:
            if not dfs(neighbor,visited,fully_explored):
                return False 
        visited.remove(course)
        fully_explored.add(course)
        return True 
    # start dfs 
    for i in range(numcourses):
        if not dfs(i,visited,fully_explored):
            return False 
    return True 

p=[[1,0],[0,1]]
print(course_schedule(2,p))       
            
    