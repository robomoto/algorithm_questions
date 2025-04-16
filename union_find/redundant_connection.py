import pytest

def redundant_connection():
    """
    You are given a tree (a connected graph with n nodes and n - 1 edges), but then one extra edge is added — forming a cycle.

    Return the edge that can be removed so the graph becomes a tree again (i.e. no cycles).

    If there are multiple answers, return the one that appears last in the input.
    """
    pass

def test_redundant_connection():
    result = redundant_connection()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
