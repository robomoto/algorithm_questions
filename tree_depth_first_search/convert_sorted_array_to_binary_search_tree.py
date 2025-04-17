import pytest

def convert_sorted_array_to_binary_search_tree():
    """
    Converts a sorted array to a height-balanced binary search tree.

    Given a sorted array of integers, the task is to convert the array into a binary search tree (BST) that is height-balanced.
    A height-balanced BST is one where the difference in the heights of the left and right subtrees of any node is at most 1.

    Args:
        nums (List[int]): A list of integers sorted in ascending order.

    Returns:
        TreeNode: The root node of the height-balanced binary search tree.
    """

    pass

def test_convert_sorted_array_to_binary_search_tree():
    result = convert_sorted_array_to_binary_search_tree()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
