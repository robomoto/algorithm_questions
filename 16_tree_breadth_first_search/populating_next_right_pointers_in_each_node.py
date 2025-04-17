import pytest

def populating_next_right_pointers_in_each_node():
    """
    Populates the next right pointer for each node in a perfect binary tree.

    Given the root of a perfect binary tree, the task is to connect each node to its next right neighbor.
    If there is no next right neighbor, the next pointer should be set to None. This operation should be done in place.

    Args:
        root (TreeNode): The root node of the perfect binary tree.

    Returns:
        TreeNode: The root node of the tree after populating all next right pointers.
    """

    pass

def test_populating_next_right_pointers_in_each_node():
    result = populating_next_right_pointers_in_each_node()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
