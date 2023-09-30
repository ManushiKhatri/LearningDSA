'''
Dijkstra's algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node (a in our case) to all other nodes in the graph.

To keep track of the total cost from the start node to each destination we will make use of the distance instance variable in the Vertex class.


+======+
• Finds the minimum-weight path between a pair of vertices in a weighted directed graph
• Solves the “one vertex, shortest path” problem in weighted graphs
• While a	vertex is still	 not known,	another	 shorter	path to it	*might* still	be found
'''
#mainly used to find the shortest path in weighted graph 
#not always shortes but the minimum value during the explore of the path
#lowest cost path problem

#implementation 
#nodes-> vertices -> weight 
#-> converting to heapify is linear time 
import heapq
#minimum cost 
def dijkstras_minimum_cost(graph,src,dst):
    heap=[] # heap will contain tuples of (cost,location)
    visited = set()
    heapq.heappush(heap,(0,src)) # 0-cost to exist at the start point 
    while heap:
        print('heap is ',heap)
        trip_cost, current = heapq.heappop(heap) # pop the first element 
        print('trip cost and current dest is',trip_cost,current)
        if current not in visited:
            visited.add(current)
        #check if we reach the destination 
        if current == dst:
            return trip_cost
        #explore the neigbors 
        for location , flight_cost in graph[current]:
            heapq.heappush(heap,(trip_cost+flight_cost,location))
    #no path to destination 
    return -1
        
    
graph ={
  'PDX': [('SFO', 160), ('JFK', 280)],
  'SFO': [],
  'JFK': [('MIA', 300), ('SFO', 410), ('SJU', 120)],
  'SJU': [('MIA', 100)],
  'MIA': [('DFW', 80)],
  'DFW': [('SJU', 100), ('JFK', 210), ('PDX', 300)]
}
print(dijkstras_minimum_cost(graph,'PDX','DFW')) #580
print(dijkstras_minimum_cost(graph,'JFK','DFW')) #300

