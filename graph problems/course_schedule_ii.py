'''

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

'''
from collections import defaultdict, deque
from typing import List
def course_schedule_ii(numCourses: int, prerequisites: List[List[int]]):
    # kahn's algorithm -> only for DAG 
    #indegree -> edges of the node 
    #first make graph 
    graph = {i:[] for i in range(numCourses)}
    for course,preq in prerequisites:
        graph[preq].append(course)
    #tracking variables 
    indegree,visited,queue = defaultdict(int),set(),deque()
    for i in range(numCourses):
        indegree[i]=0
    for vertex,edge in graph.items():
        for v in edge:
            indegree[v]+=1
    #iterate through indegre to find the starting node 
    for node,degree in indegree.items():
        if not degree:
            queue.append(node)
    print('graph , indegree',graph,indegree)
    print('queue is',queue)
    final_answer = []
    count = 0 #to detect the cycle 
    #process the queue 
    while queue:
        node = queue.popleft()
        count += 1
        visited.add(node)
        final_answer.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
    print('count is',count)
    if count!= numCourses:
        return []
    return final_answer

# Test
p=[[1,0],[2,0],[3,1],[3,2]]
print(course_schedule_ii(4,p)) # [0,2,1,3] expected 
