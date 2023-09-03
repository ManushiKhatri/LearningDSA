'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


'''
from tree_node import *

def path_sum(root, target):
    if not root:
        return False 

    def dfs(node, remaining_sum):
        if not node:
            return False
        print(f"Visiting node: {node.val}) remaining_sum: {remaining_sum}")
        # Subtract the node's value from the remaining sum
        remaining_sum -= node.val
        # If it's a leaf node, check if the remaining sum is zero
        if not node.left and not node.right:
            return remaining_sum == 0
        # Recursively check the left and right children
        return dfs(node.left, remaining_sum) or dfs(node.right, remaining_sum)

    return dfs(root, target)

root = root_from_list([5,4,8,11,None,13,4,7,2,None,None,None,1])
pretty_print(root)
print(path_sum(root, 22))  # Should return True

root=root_from_list([1,2,3])
pretty_print(root)
print(path_sum(root,5))#false
