import pytest

def binary_tree_paths():
    """
    Finds all root-to-leaf paths in a binary tree.

    Given the root of a binary tree, the task is to return all root-to-leaf paths in the tree. Each path is represented
    as a string of node values from the root to a leaf node, separated by '->'.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        List[str]: A list of strings, where each string represents a root-to-leaf path in the binary tree.
    """


    pass

def test_binary_tree_paths():
    result = binary_tree_paths()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
