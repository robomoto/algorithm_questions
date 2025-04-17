import pytest

def vertical_order_traversal_of_a_binary_tree():
    """
    Performs a vertical order traversal of a binary tree.

    Given the root of a binary tree, the task is to return the vertical order traversal of its nodes' values. 
    In vertical order traversal, nodes are visited column by column from left to right, and at each column, 
    nodes are visited from top to bottom.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        List[List[int]]: A list of lists, where each inner list contains the node values for a specific vertical 
                         column, from top to bottom, from left to right.
    """

    pass

def test_vertical_order_traversal_of_a_binary_tree():
    result = vertical_order_traversal_of_a_binary_tree()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
