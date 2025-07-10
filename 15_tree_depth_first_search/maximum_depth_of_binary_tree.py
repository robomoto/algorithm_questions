"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100"""

import pytest
from typing import Union

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximum_depth_of_binary_tree(root: Union[TreeNode, None]) -> int:
  if root is None:
      return 0
  return max_depth_helper(root, 1)
  

def max_depth_helper(node: TreeNode, depth: int):
    if node is None:
        return depth
    left, right = 0, 0
    if node.left:
        left = max_depth_helper(node.left, depth+1)
    if node.right:
        right = max_depth_helper(node.right, depth+1)
    return max(depth, left, right)

def test_maximum_depth_of_binary_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n6
    result = maximum_depth_of_binary_tree(n1)
    assert result == 4

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
