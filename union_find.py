'''
You are given a list of centers of 2D objects on a plane.
Each object has a square bounding box. 
Two objects are said to collide if the distance between their centers in both the x and y directions does not exceed 2. Your task is to determine how many pairs of objects have collision boxes that intersect.

'''



def solution(centers):
    parent = list(range(len(centers)))
    print('parent before',parent)
    rank = [1] * len(centers)
    collisions = 0  # Counter for collisions

    def find(n):
        if parent[n] != n:
            parent[n] = find(parent[n])
        return parent[n]

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return False  # No new union made
        if rank[p1] < rank[p2]:
            parent[p1] = p2
        elif rank[p1] > rank[p2]:
            parent[p2] = p1
        else:
            parent[p2] = p1
            rank[p1] += 1
        return True  # Successful union

    def collision(coord1, coord2):
        return abs(coord1[0] - coord2[0]) <= 2 and abs(coord1[1] - coord2[1]) <= 2
    count = 0
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            if collision(centers[i], centers[j]):
                if union(i,j):
                    count += 1
    print('parent is',parent)
    return count 

# Testing the solution

centers = [
    [-100000, -100000],
    [-100000, -100000],
    [100000,-100000 ],
    [100000,100000]
]
print(solution(centers))  # Expected output: 0 # got 1 


