import pytest

def flatten_binary_tree_to_linked_list():
    """
    Flattens a binary tree to a linked list in-place.

    Given the root of a binary tree, the task is to flatten the tree into a linked list in-place. The flattened tree should 
    follow the same structure as a singly linked list, where the left child of each node is null and the right child is the 
    next node in the list.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        None: The binary tree is flattened in-place.
    """

    pass

def test_flatten_binary_tree_to_linked_list():
    result = flatten_binary_tree_to_linked_list()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
