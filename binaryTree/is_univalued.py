'''
A binary tree is univalued if and only if every node in the tree contains the same value. Write a function that receives the root of a binary tree as input and determines if the given tree is univalued. Feel free to write a helper (recursive) method.

Examples:

        7 
      /    \
    3      10           →  False
  /   \   /   \
-1    5   9    12

        5 
      /    \
     5      5 
     →  True
     
        7 
      /    \
    7       7           →  False
  /   \     / 
 7     7   8 
   
        3 
      /    \
    3      3           →  true
         /   \
        3     3


'''
from tree_node import *
def is_univalued(root):
    if not root:
        return True 
    if root.left:
        if root.left.val != root.val:
            return False 
    if root.right:
        if root.right.val!=root.val:
            return False 
    return is_univalued(root.left) and is_univalued(root.right)
        
    return  dfs(root,root.val)
root=root_from_list([3,3,1])#True 
pretty_print(root)
print(is_univalued(root))

        