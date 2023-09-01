
'''
Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always None.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
BIG HINT: MAYBE POST ORDER WOULD DO YOU JUSTICE!!!!!!
Examples
Diagram:

Input: root = [1,2,5,3,4,None,6]
Output: [1,None,2,None,3,None,4,None,5,None,6]

'''
from tree_node import *
from visualiser.visualiser import Visualiser as vs

@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def flatten(root):
  def helper(root):
    if not root: 
        return None
    left = helper(root.left)
    right = helper(root.right)
    root.left = None
    root.right = left
    
    if not root.right:
        root.right = right
    else:
      temp = root.right
      while temp.right: 
          temp = temp.right
      temp.right = right
    return root
  return helper(root)
root = root_from_list([1,2,5,3,4,None,6])
pretty_print(root)
pretty_print(flatten(root))

