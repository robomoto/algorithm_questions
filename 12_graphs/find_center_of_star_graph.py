import pytest

def find_center_of_star_graph():
    """
    Finds the center node of a star graph.

    A star graph is a tree with one central node that is directly connected to all other nodes.
    The task is to find the center node of the given star graph.

    Args:
        edges (List[List[int]]): A list of edges representing the graph, where each edge is a list of two integers.

    Returns:
        int: The center node of the star graph.
    """

    pass

def test_find_center_of_star_graph():
    result = find_center_of_star_graph()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
