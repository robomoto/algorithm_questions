import pytest

def inorder_successor_in_bst():
    """
    Finds the inorder successor of a node in a Binary Search Tree (BST).

    Given a node in a binary search tree, the task is to find the inorder successor of that node. The inorder successor of a node 
    is the next node in the inorder traversal of the tree. If the node has a right child, the successor is the leftmost node 
    in the right subtree. If the node does not have a right child, the successor is one of its ancestors.

    Args:
        root (TreeNode): The root node of the binary search tree.
        p (TreeNode): The node for which to find the inorder successor.

    Returns:
        TreeNode: The inorder successor of the given node, or None if no successor exists.
    """

    pass

def test_inorder_successor_in_bst():
    result = inorder_successor_in_bst()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
