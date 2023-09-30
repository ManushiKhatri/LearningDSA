'''
input 

wins = [3,1,2,2]
draws=[1,5,4,4]
scored=[30,10,20,40]
conceded=[32,13,18,17]

'''
import heapq

def winners(wins,draws,scored,conceded):
    heap =[]
    for i in range(len(wins)):
        points = (wins[i]*3)+ draws[i]
        goal_difference=(scored[i]-conceded[i])
        heap.append((-points,-goal_difference,-i))
    print('heap is',heap)
    final_output =[]
    heapq.heapify(heap)
    for i in range(2):
        final_output.append(-heapq.heappop(heap)[2])
    return final_output
       
 
wins = [7,1,6,2]
draws=[4,5,4,4]
scored=[30,10,20,40]
conceded=[32,13,18,17]
print(winners(wins,draws,scored,conceded))