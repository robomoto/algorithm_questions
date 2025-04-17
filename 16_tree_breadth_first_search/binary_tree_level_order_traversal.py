import pytest

def binary_tree_level_order_traversal():
    """
    Performs a level-order traversal of a binary tree.

    Given the root of a binary tree, the task is to return the level-order traversal of its nodes' values. 
    In a level-order traversal, nodes are visited from top to bottom and from left to right at each level.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        List[List[int]]: A list of lists where each inner list represents the values of the nodes at each level.
    """

    pass

def test_binary_tree_level_order_traversal():
    result = binary_tree_level_order_traversal()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
