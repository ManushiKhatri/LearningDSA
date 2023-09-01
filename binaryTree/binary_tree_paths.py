'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Examples
Diagram:

Input: root = [1,2,3,None,5]
Output: ["1->2->5","1->3"]



'''
from tree_node import *
def binary_tree_paths(root):
    if not root:
        return []
    final_output=[]
    def dfs(node,level):
        if not node:
            return 
        # print('level is',level)
        level.append(str(node.val))
        if not node.left and not node.right:
            # leaf node
            final_output.append('->'.join(level[:]))
        dfs(node.left,level)
        dfs(node.right,level)
        level.pop()        
    dfs(root,[])
    return final_output
root = root_from_list([1,2,3,None,5])
pretty_print(root)
print(binary_tree_paths(root))
root = root_from_list([3, 9, 20, None, None, 15, 7])
pretty_print(root)
print(binary_tree_paths(root))

#time complexity would be O(n)-> in the worst case we need to visit every nodes 
# space complexity would be O(height of recursive call)