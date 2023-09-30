'''
Problem: Write a method that receives the root of a binary tree and returns the tree's height.


height Of binary tree at the start root is defined to be zero

'''
from tree_node import *
from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def binary_tree_height(root):
    #base case 
    if not root:
        return -1
    left_height = binary_tree_height(root.left)
    right_height=binary_tree_height(root.right)
    return max(left_height,right_height)+1 # since only single root has height 0 so to negotiate that
root = root_from_list([3, 9, 20, None, None, 15, 7])
root1 = root_from_list([3])
print(binary_tree_height(root))#2
print(binary_tree_height(root1))#0

def main():
    # Call function
    print(binary_tree_height(root))
    # Save recursion tree to a file
    vs.make_animation("visualize/binarytreeheight.gif", delay=2)
if __name__ == "__main__":
    main()     
    