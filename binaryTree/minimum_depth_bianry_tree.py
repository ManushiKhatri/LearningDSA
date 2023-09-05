'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:


Input: root = [3,9,20,None,None,15,7]
Output: 2
Example 2:

Input: root = [2,None,3,None,4,None,5,None,6]
Output: 5

'''
'''
Sure, let's break down how the recursive code works by taking an example.

Let's consider the following binary tree:

```
       1
     /   \
    2     3
   / \
  4   5
```

Now, let's call `minDepth` on the root node (node with value 1).

1. Node `1` is the root and is not `None`.
2. Node `1` has both left and right children.
3. So, we recursively call `minDepth` on its left child (node `2`) and its right child (node `3`) and take the minimum of the two.

   - For Node `2`:
     1. It's not `None`.
     2. It has both left and right children.
     3. Again, recursively call `minDepth` on its left child (node `4`) and right child (node `5`).

       - For Node `4`:
         1. It's a leaf node (no children).
         2. Return `1`.

       - For Node `5`:
         1. It's also a leaf node.
         2. Return `1`.

     4. Node `2` will get `1` from both of its children, then it adds `1` to the minimum of these two values (which is `1`), and returns `2`.

   - For Node `3`:
     1. It's a leaf node (no children).
     2. Return `1`.

4. Node `1` will get `2` from its left child (node `2`) and `1` from its right child (node `3`). It adds `1` to the minimum of these two values (which is `1`), and returns `2`.

The overall `minDepth` of this tree is `2`.

The recursion basically breaks down the tree into smaller and smaller problems until we reach the base case (leaf nodes). Each leaf node returns a depth of `1`, and as the recursive calls return to their parent nodes, we add `1` to the depth of the deeper child node. The process continues until we reach the root and get the minimum depth of the entire tree.


'''
from tree_node import *
def minimum_depth(root):
    #base case 
    if not root:
        return 0
    #both leaf node
    if root.left and root.right:
        return min(minimum_depth(root.left),minimum_depth(root.right))+1
    elif root.right:
        return minimum_depth(root.right)+1
    elif root.left:
        return minimum_depth(root.left)+1
    return 1 
root = root_from_list([3,9,20,None,None,15,7])
pretty_print(root)
print(minimum_depth(root)) # 2 
