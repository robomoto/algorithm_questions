import pytest

def kth_smallest_element_in_a_bst():
    """
    Finds the k-th smallest element in a Binary Search Tree (BST).

    Given the root of a Binary Search Tree and an integer k, the task is to find the k-th smallest element in the BST. 
    In a BST, the left subtree contains smaller elements, and the right subtree contains larger elements.

    Args:
        root (TreeNode): The root node of the Binary Search Tree.
        k (int): The index (1-based) of the smallest element to find.

    Returns:
        int: The k-th smallest element in the Binary Search Tree.
    """

    pass

def test_kth_smallest_element_in_a_bst():
    result = kth_smallest_element_in_a_bst()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
