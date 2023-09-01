'''
 Remove Leaves
Given the root of a tree, remove all of its leaf nodes.

root = root_from_list([3, 9, 20, None, None, 15, 7])
expected = 3 None 20

'''
from tree_node import *
def remove_leaves(root):
    #note-> make the return on every call constant 
    if not root:
        return None 
    if not root.left and not root.right:
        return None 
    root.left = remove_leaves(root.left)
    root.right= remove_leaves(root.right)
    return root 
root = root_from_list([3, 9, 20, None, None, 15, 7])
pretty_print(root)
pretty_print(remove_leaves(root))

    

