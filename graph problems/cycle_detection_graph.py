'''
Cycle Detection

Cycle Detection: Pseudocode (adapted from source, wiki)

procedure has_cycle(G)
    for all vertices v
        v.status ←  NEW
    for all vertices v
        if v.status = NEW (AKA UNVISITED)
            if has_cycle_dfs(v):
                return True
    return False

procedure has_cycle_dfs(v)
    v.status = PRE (AKA STARTED)

    for each edge v → w
        if w.status = PRE 
            return True
        if w.status = NEW
            if has_cycle_dfs(w) = True
                return True

    v.status = POST (AKA FINISHED)
    return False
    
'''
#converting algorithm into code 
# let's try for directed graph -> one direction 
def cycle_detection_dg(graph):
    #helper function 
    def has_cycle_dfs(vertex,status):
        status[vertex]='PRE' #visiting
        for neighbor in graph[vertex]:
            if status[neighbor]=='PRE':
                return True # detected cycle 
            if status[neighbor]=='NEW':
                if has_cycle_dfs(neighbor,status):
                    return True 
        status[vertex]='POST'
        return False 
    status = {}
    for vertex in graph:
        status[vertex]='NEW' #initally setting all nodes as pre (not visited)
    for vertex in graph:
        if status[vertex]=='NEW':
            if has_cycle_dfs(vertex,status):
                return True 
    return False 
def cycle_detection_ug(graph):
    #helper function 
    def has_cycle_dfs(vertex,status):
        status[vertex]='PRE' #visiting
        for neighbor in graph[vertex]:
            if status[neighbor]=='PRE':
                continue 
            if status[neighbor]=='NEW':
                if has_cycle_dfs(neighbor,status):
                    return True 
        status[vertex]='POST'
        return False 
    status = {}
    for vertex in graph:
        status[vertex]='NEW' #initally setting all nodes as pre (not visited)
    for vertex in graph:
        if status[vertex]=='NEW':
            if has_cycle_dfs(vertex,status):
                return True 
    return False 
       
       
graph = {
    'A': ['B'],
    'B': ['A','D'],
    'C': ['D', 'E'],
    'D': ['B'],  # This creates a cycle: B -> C -> D -> B
    'E': [] #no outgoing edges 
}
print(cycle_detection_dg(graph))
print(cycle_detection_ug(graph))

def find_path(graph):
    if not graph:
        return []
    result=[]
    visited=set()
    def dfs(node):
        if node in visited:
            return result 
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        return result
    for key in graph:
        return dfs(key)
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': [],
    'D': ['A'],
    'E':['F']
}
print(find_path(graph))