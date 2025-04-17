import pytest

def convex_polygon():
    """
    Determines if a set of points form a convex polygon.

    A polygon is convex if all of its interior angles are less than 180 degrees, or equivalently, if all its 
    vertices are on the outside of the polygon. Given a set of points representing the vertices of a polygon, 
    the task is to check if the polygon formed by these points is convex.

    Args:
        points (List[List[int]]): A list of points where each point is represented as [x, y], representing the vertices of the polygon.

    Returns:
        bool: True if the points form a convex polygon, False otherwise.
    """

    pass

def test_convex_polygon():
    result = convex_polygon()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
