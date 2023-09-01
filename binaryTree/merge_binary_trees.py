'''
Merge Two Binary Trees
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT None node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Examples
Diagram:

Input: root1 = [1,3,2,5], root2 = [2,1,3,None,4,None,7]
Output: [3,4,5,5,4,None,7]


'''
from tree_node import * 

def merge_binary_trees(root1,root2):
    #base case 
    if not root1 and not root2:
        return None 
    if not root1 and root2:
        return root2
    if not root2 and root1:
        return root1

    #lets do pre oder traversal -> root_> left-> right
    new_merged_value = root1.val + root2.val 
    print('new merged value is',new_merged_value)
    new_tree=TreeNode(new_merged_value)
    new_tree.left=merge_binary_trees(root1.left,root2.left)
    new_tree.right=merge_binary_trees(root1.right,root2.right)
    return new_tree
root1=root_from_list([1,3,2,5])
root2=root_from_list([2,1,3,None,4,None,7])
print("===root1==")
pretty_print(root1)
print()
print("===root2==")
pretty_print(root2)
print('==merged root===')
m=merge_binary_trees(root1,root2)
pretty_print(m)
    