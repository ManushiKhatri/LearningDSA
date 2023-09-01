'''
Given a binary tree, determine if it is height-balanced. 
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Examples
Diagram:

Input: root = [3,9,20,None,None,15,7]
Output: True
Explanation: This function takes in a TreeNode as the root. We can represent the tree as an array as shown in the input. If you take that array and use the `root_from_list` helper method, it will convert the list into a Tree!

Diagram:

Input: root = [1,2,2,3,3,None,None,4,4]
Output: false


'''
#height balanced tree is depth=0 as base case 
from tree_node import *

def is_balanced(root):
    if not root:
        return True 
    def helper(node):
        #base case 
        if not node:
            return 0 # O(1)
        return max(helper(node.left),helper(node.right))+1 
    left_height=helper(root.left)
    right_height=helper(root.right)
    if abs(left_height-right_height) > 1:
        return False 
    return is_balanced(root.left) and is_balanced(root.right)

root = root_from_list([1,2,2,3,3,None,None,4,4])
root1=root_from_list([3,9,20,None,None,15,7])
pretty_print(root)
print(is_balanced(root)) #return false 
pretty_print(root1)
print(is_balanced(root1)) #true  

# Time Complexity 
# T(n)= 2 * T(n/2)
#0(n)+1 = O(n) in the worst case 
#space comlexity = height of recursion call in the worst case it would be O(n)-> calling eevery function