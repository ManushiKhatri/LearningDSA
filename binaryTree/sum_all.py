'''
Problem: Write a method that receives the root of a binary tree and returns the sum of all the values stored in it.

'''
from tree_node import *
def sum_all_value(root):
    if not root:
        return 0
    sum_left=sum_all_value(root.left)
    sum_right=sum_all_value(root.right)
    return root.val + sum_left + sum_right
    
root = root_from_list([3, 9, 20, None, None, 15, 7])
# pretty_print(root)
print(sum_all_value(root))
    

    