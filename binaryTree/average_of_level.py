'''
 Average of Levels in Binary Tree
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

Examples
Diagram:

Input: root = [3,9,20,None,None,15,7]
Output: [3.00000,14.50000,11.00000]

'''
from tree_node import *
from collections import deque
def average_level(root):
    if not root:
        return []
    q =deque()
    q.append(root)
    q.append(None)#to know the level
    final_output,level=[],[]
    while q:
        # print('q is',q)
        node = q.popleft()
        if node:
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        else:
            final_output.append(sum(level)/len(level))
            level = []
            #adding another layer of level 
            if q:
                q.append(None)
    return final_output
root = root_from_list([3,9,20,None,None,15,7])
pretty_print(root)
print(average_level(root))
    
        
        