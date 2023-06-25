from collections import *
''''
input : [['Adam', 'Amy'], ['Adam', 'Howard'], ['Howard', 'Angela'],
         ['Howard', 'Barry'], ['Angela', 'Carla'], ['Carla', 'Adam']]

expectd : {'Adam': {'Howard', 'Amy'},
          'Howard': {'Angela', 'Barry'},
         'Angela': {'Carla'}, 
         'Carla': {'Adam'}}


'''

'''  Making adjacency lists '''
edges = [['Adam', 'Amy'], ['Adam', 'Howard'], ['Howard', 'Angela'],
         ['Howard', 'Barry'], ['Angela', 'Carla'], ['Carla', 'Adam']]
def create_adj_list(edges: list[list[str]]) -> dict:
  if not edges: return {}
  graph = defaultdict(set)
  for edge in edges:
    graph[edge[0]].add(edge[1])
  return dict(graph)



print(create_adj_list(edges))

''' making adjacency matrix '''

def create_adj_matrix(edges: list[list[str]]) -> list[list[int]]:
  if not edges: return []

  # Create Vertices
  vertices = set()
  for edge in edges:
    vertices.add(edge[0])
    vertices.add(edge[1])

  # Map vertices to index
  vertex_to_index = {}
  index = 0
  for vertex in vertices:
    vertex_to_index[vertex] = index
    index += 1

  # Create matrix.
  matrix = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]

  for edge in edges:
    src_index = vertex_to_index[edge[0]]
    dest_index = vertex_to_index[edge[1]]
    matrix[src_index][dest_index] = 1
  return matrix
print(create_adj_matrix(edges))
