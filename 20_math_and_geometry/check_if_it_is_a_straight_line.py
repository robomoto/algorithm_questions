import pytest

def check_if_it_is_a_straight_line():
    """
    Determines if a set of points lie on a straight line.

    Given a list of points, the task is to check if all the points lie on the same straight line.
    The points are represented as pairs of coordinates (x, y), and the function checks if the points are collinear.

    Args:
        coordinates (List[List[int]]): A list of points, where each point is represented as [x, y].

    Returns:
        bool: True if the points lie on a straight line, False otherwise.
    """

    pass

def test_check_if_it_is_a_straight_line():
    result = check_if_it_is_a_straight_line()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
