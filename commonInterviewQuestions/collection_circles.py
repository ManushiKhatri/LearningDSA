
'''Problem: A circle is define by x-axis position, y-axis position, and a radius.
A circle group is a collection of circles that overlap. 
Given a list of circles, figure out if they belong to a single circle group.
Formula for calculating distance between two points: sqrt((x2-x1)^2 + (y2-y1)^2)


*****===Explanation===**
Alright! Let's visualize the process step-by-step using tracing, especially on the example [[2, 1, 3], [6, 1, 4], [8, 1, 5]].

We'll start by setting up our basic Union-Find structure:

Initialization:

We have 3 circles, so len(circles) = 3.
parent = [0, 1, 2] meaning each circle is its own parent.
rank = [1, 1, 1] meaning each circle's set has a rank of 1.
Visualization:

makefile
Copy code
Circles:    A       B       C
           [2,1,3] [6,1,4] [8,1,5]
parent:    0       1       2
rank:      1       1       1
Processing:

We'll iterate through each pair of circles to check if they overlap:

Check overlap between A and B:
They overlap because the distance between A and B is 4 and 3 + 4 = 7 which is greater than 4.
Therefore, union A and B:
Find the parent of A (returns 0)
Find the parent of B (returns 1)
Since both have the same rank, we'll make B a child of A and increase the rank of A.
parent becomes [0, 0, 2] and rank becomes [2, 1, 1].
Visualization:

makefile
Copy code
Circles:    A       B       C
           [2,1,3] [6,1,4] [8,1,5]
parent:    0       0       2
rank:      2       1       1
Sets:      {A, B}  -       {C}
2. Check overlap between A and C:

They don't overlap directly. So, no changes.
Check overlap between B and C:
They overlap because the distance between B and C is 2 and 4 + 5 = 9 which is greater than 2.
Therefore, union B and C:
Find the parent of B (returns 0 because B is now a child of A)
Find the parent of C (returns 2)
We'll make C a child of A (since A has the higher rank).
parent becomes [0, 0, 0] and rank becomes [3, 1, 1].
Visualization:

makefile
Copy code
Circles:    A       B       C
           [2,1,3] [6,1,4] [8,1,5]
parent:    0       0       0
rank:      3       1       1
Sets:      {A, B, C}
Final Result:

Since all circles are in the same set ({A, B, C}), they all belong to a single circle group.
Summary:

The Union-Find algorithm allowed us to efficiently group circles that overlap.
The find function identifies the ultimate parent (or root) of each circle.
The union function connects two circles (or more specifically, their sets) together if they overlap.
At the end, if all circles share the same root (or belong to the same set), they are part of a single circle group.


'''
# questions seem to be  union find algorithm 
#[x,y,r]

import math 
def sqrt_function(circle1, circle2):
    dist = math.sqrt((circle2[0] - circle1[0])**2 + (circle2[1] - circle1[1])**2)
    sum_of_radii = circle1[2] + circle2[2]
    print(f"Distance between centers: {dist}, Sum of Radii: {sum_of_radii}")
    return dist <= sum_of_radii


def circle_group(circles):
    parent=list(range(len(circles))) # n nodes 
    rank = [1]*len(circles) # rank -> determining the size 
    def find(n):
        if parent[n]!=n:
            #path compression 
            parent[n] = parent[parent[n]]
            n=parent[n]
        return n
    def union(n1,n2):
        p1,p2 = find(n1),find(n2)
        if p1==p2:
            return 
        elif rank[p1] < rank[p2]:
            parent[p1]=p2
            rank[p1] += 1
        else:
            parent[p2]=p1
            rank[p2]+=1
    # processing the edges 

    for i in range(len(circles)):
        for j in range(i+1,len(circles)):
            test=sqrt_function(circles[i], circles[j])
            if test:
                print(f"Connecting circle {i} with circle {j} {test}")
                f=union(i, j)
                print('f is',f)
    print('parent and rank is',parent,rank)
    unique_parents = set()
    for i in range(len(circles)):
        parent_i=find(i)
        print('parent i is',parent_i)
        unique_parents.add(parent_i)
    print("Unique Parents:", unique_parents)
    return len(unique_parents)==1
    


circles = [[2,1,3],[6,1,4]]
assert circle_group(circles) == True, "The two circles do not belong to a single circle group."

circles = [[2, 1, 3], [6, 1, 4], [8, 1, 5]]
print(circle_group(circles))  == True # Output: True (all three circles overlap)

circles = [[2, 1, 3], [6, 1, 4], [10, 1, 4]]
print(circle_group(circles))  == False # Output: False (the third circle does not overlap with the other two circles)

circles = [[2, 1, 3], [2, 2, 3], [2, 3, 3]]
print(circle_group(circles)) == True # Output: True (all three circles are the same circle)

circles = [[0, 0, 1], [3, 0, 1], [10, 0, 1]]
print(circle_group(circles))  == False

circle=[[0, 0, 2], [2, 0, 1], [5, 0, 1]]
print(circle_group(circle)) == False # a c doesnot overlap b c doesnot overlap 