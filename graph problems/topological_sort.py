'''

Aside from DFS and BFS, the most common graph concept that interviews will test is topological sorting. Topological sorting produces a linear ordering of nodes in a directed graph such that the direction of edges is respected.

A topological sort is an ordering of nodes for a directed acyclic graph (DAG) such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

Topological sort is simply a modification of DFS. Topological sort simply involves running DFS on an entire graph and adding each node to the global ordering of nodes, but only after all of a node's children are visited. This ensures that parent nodes will be ordered before their child nodes, and honors the forward direction of edges in the ordering.

* directed acylic graph

'''
from collections import deque
def top_sort(graph):
    sorted_nodes, visited = deque(), set()
    def dfs(graph, start_node, visited, sorted_nodes):
        visited.add(start_node)
        if start_node in graph:
            neighbors = graph[start_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs(graph, neighbor, visited, sorted_nodes)
        sorted_nodes.appendleft(start_node) #0(1)
    for node in graph:
        if node not in visited:
           dfs(graph, node, visited, sorted_nodes)
    return list(sorted_nodes)
graph = {
    'A': ['B'],
    'B': ['A','D'],
    'C': ['D', 'E']
} 
prerequisites = {
  "Economics": ["Algebra"],
  "Calculus": ["Algebra"],
  "Algebra": [],
  "Chemistry": ["Algebra"],
  "Biology": [],
  "Differential Equations": ["Calculus"],
  "Physics": ["Algebra"],
  "Electronics": ["Physics", "Computer Science"],
  "Quantum Physics": ["Differential Equations", "Physics"],
  "Computer Science": [],
  "Bioinformatics": ["Computer Science", "Biology"]
}

print(top_sort(graph))  
print(top_sort(prerequisites))  

print("=== bfs approach ==")
from collections import defaultdict
def topological_sort_bfs(graph):
  if not graph: return []

  q, result, visited, indegree = deque(), [], set(), defaultdict(int)
  for src, edges in graph.items():
    print('src and ege is',src,edges)
    if src not in indegree: 
        indegree[src] = 0
    for vertex in edges: 
        indegree[vertex] += 1
    print('indegree us',indegree)

  for vertex, degree in indegree.items():
    if not degree: 
        q.append(vertex)
  
  print('q iis',q)
  while q:

    node = q.popleft()
    if node in visited: 
        return []
    visited.add(node)
    result.append(node)
    for neighbor in graph.get(node, []):
      indegree[neighbor] -= 1
      if not indegree[neighbor]: 
          q.append(neighbor)
  return result
prerequisites = {
  "Economics": ["Algebra"],
  "Calculus": ["Algebra"],
  "Algebra": [],
  "Chemistry": ["Algebra"],
  "Biology": [],
  "Differential Equations": ["Calculus"],
  "Physics": ["Algebra"],
  "Electronics": ["Physics", "Computer Science"],
  "Quantum Physics": ["Differential Equations", "Physics"],
  "Computer Science": [],
  "Bioinformatics": ["Computer Science", "Biology"]
}
print(topological_sort_bfs(prerequisites))
