import pytest

def lowest_common_ancestor_of_a_binary_tree_iii():
    """
    Given the root of a binary tree and two nodes p and q, return the lowest common ancestor (LCA) of the two nodes.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor of two nodes p and q in a binary tree is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    A descendant of a node x is a node y that is on the path from node x to some leaf node.
    A node is a descendant of itself.
    """
    pass

def test_lowest_common_ancestor_of_a_binary_tree_iii():
    result = lowest_common_ancestor_of_a_binary_tree_iii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
