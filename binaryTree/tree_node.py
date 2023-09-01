class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)

def pretty_print(root, depth=0):
  """helper method prints out the tree oriented horizontally, a 90 degree
     rotation from the usual top-down view."""
  if not root:
    return
  pretty_print(root.right, depth + 1)
  print(depth * "   " + str(root.val))
  pretty_print(root.left, depth + 1)


def root_from_list(lst):

  def helper(i):
    if i >= len(lst) or not lst[i]:
      return None

    return TreeNode(lst[i], helper(2 * i + 1), helper(2 * i + 2))
  return helper(0)

root = root_from_list([3, 9, 20, None, None, 15, 7])
# pretty_print(root)