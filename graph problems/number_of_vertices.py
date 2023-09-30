'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]


'''
from typing import List 
def findCircleNum(isConnected: List[List[int]]) -> int:
    parent=list(range(len(isConnected)))
    rank = [1]*len(isConnected)
    def find(node):
        while node != parent[node]:
            #pathe copmpression 
            parent[node]=parent[parent[node]]
            node = parent[node]
        return node 
    def union(n1,n2):
        p1,p2=find(n1),find(n2)
        if p1==p2:
            return 
        elif rank[p1]>rank[p2]:
            parent[p2]=p1
            rank[p1]+=1
        else:
            parent[p1]=p2
            rank[p2]+=1
    for i in range(len(isConnected)):
        for j in range(len(isConnected)):
            if isConnected[i][j]==1:
                union(i,j)
    print('parent is',parent)
    # find actual parent node for every node 
    return len(set(find(p) for p in parent))
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(isConnected)) == 3
 
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(isConnected)) == 2
 