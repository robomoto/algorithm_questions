import pytest

def binary_tree_zigzag_level_order_traversal():
    """
    Performs a zigzag level-order traversal of a binary tree.

    Given the root of a binary tree, the task is to return the zigzag level-order traversal of its nodes' values.
    In a zigzag level-order traversal, nodes are visited level by level, but at each level, the order of visiting
    nodes alternates between left-to-right and right-to-left.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        List[List[int]]: A list of lists where each inner list represents the values of the nodes at each level, 
                         with the zigzag traversal order.
    """

    pass

def test_binary_tree_zigzag_level_order_traversal():
    result = binary_tree_zigzag_level_order_traversal()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
