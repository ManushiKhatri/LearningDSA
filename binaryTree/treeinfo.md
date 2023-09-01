## Types Of Tree Traversal

---

### 1. Preorder Traversal
**Order**: 
- Root
- Left 
- Right 

**Description**:
- Begin from the root.
- Traverse the left subtree before the right subtree.
- In the subtree, the same logic applies: visit the root of the subtree first, then the left child and finally the right child.

---

### 2. Inorder Traversal
**Order**: 
- Left
- Root
- Right

**Description**:
- Begin from the leftmost node.
- After traversing the left subtree, visit the root.
- Finally, traverse the right subtree.
- This traversal, when applied on a binary search tree, visits the nodes in ascending order.

---

### 3. Post Order Traversal
**Order**:
- Left
- Right
- Root

**Description**:
- Begin from the leftmost node.
- Traverse the entirety of the left and right subtrees before visiting the root node.
- This kind of traversal is useful when deleting nodes from a tree, as children are deleted before their parent.

---

### 4. Level Order Traversal
**Description**:
- Also known as Breadth-First Search (BFS) for trees.
- Start at the root, and visit nodes level by level.
- Traverse all nodes of the current depth (or level) before moving on to nodes of the next depth.
- It's similar to how you might read English text: left to right, top to bottom.


---
### BINARY TREE PROPERTIES

- A binary tree is a tree in which each node must have no more than two children.
- The max total number of nodes in a binary tree is  2ℎ+1−1 , where  ℎ  is the height of the tree. 
- The number of nodes at any level of a binary tree is at most  2L , where  L  is the 0-indexed level of the node. (e.g. at level 1 there is a max of 21 nodes or 2 nodes

---
### Tree Recursion Working Mechanism 

![My Picture](recursionwork.png)
