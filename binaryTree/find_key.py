'''
Problem: Write a method that receives the root of a binary tree and a key, and determines if the key is in the tree.


tree = 1 2 3 4 5 6 7 
key : 3 
return True 
9
else return False 

'''
from tree_node import *
def find_key(root,key):
    #base case 
    if not root:
        return False 
    if root.val==key:
        return True 
    return find_key(root.left,key) or find_key(root.right,key)
root = root_from_list([3, 9, 20, None, None, 15, 7])
print(find_key(root,3)) #True
print(find_key(root,19))#False 
print(find_key(root,7))#True 

    
    