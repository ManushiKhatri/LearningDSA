'''
Given the root of a tree, remove all nodes where the sum of the nodes on the path from root to that node (including that node) is greater than limit.

Example:

Given the initial tree
root ->  3
       4   2
     1
calling limit_path(root, 6), would result in the following tree:
root -> 3
          2
this is because the path to node 4 exceeded the given limit (ie: 3 + 4 > 6) so it and all its descendents were removed from the tree.


'''
#pass by value will change so be careful on what you declare and add 
from tree_node import *
def limit_path(root, limit):
    if not root:
        return root
    def leafNode(node):
        return not node.left and not node.right
    
    def dfs(node, summ):
        if not node:
            return None
        
        summ += node.val
        # Recursively prune children first
        node.left = dfs(node.left, summ)
        node.right = dfs(node.right, summ)

        # If the current node is a leaf and its path sum is less than the limit
        if summ >= limit and leafNode(node):
            return None
        return node
    return dfs(root, 0)

root = root_from_list([3,4,2,1])
pretty_print(root)
print("=====")
limit_path(root,6)
pretty_print(root)
    
    