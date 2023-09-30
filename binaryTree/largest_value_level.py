'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).


Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]



'''
from collections import deque
import math
from tree_node import *
def largest_value(root):
    if not root:
        return None 
    q=deque()
    q.append(root)
    q.append(None)
    max_value = -math.inf 
    result = []
    while q:
        node = q.popleft()
        if node:
            #processed for that level 
            max_value = max(max_value,node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        else:
            #we reached the level 
            result.append(max_value)
            max_value=-math.inf
            if q:
                q.append(None)
    return result 
root=root_from_list([1,3,2,5,3,None,9])
print(largest_value(root))#[1,3,9]   