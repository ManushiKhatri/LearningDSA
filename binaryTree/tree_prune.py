'''
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

'''
from tree_node import root_from_list,pretty_print
def prune_tree(root):
    if not root:
        return None 
    #do post order traversal
    def dfs(node):
        #base case 
        if not node:
            return None
        # case 1: check if the node is leaf node or not 
        node.left=dfs(node.left)
        node.right=dfs(node.right)
        if not node.left and not node.right:
            if node.val !=1 :
                return None 
        return node 
    return dfs(root)
root = root_from_list([1,2,2,2,2,2,1])
pretty_print(root)
print("==root after pruning ")
pretty_print(prune_tree(root))

