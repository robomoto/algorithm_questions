import pytest

def number_of_islands():
    """
    Given a 2D grid of '1's (land) and '0's (water), count the number of islands.

    An island is formed by connecting adjacent lands horizontally or vertically.

    You may assume all four edges of the grid are surrounded by water.
    """
    pass

def test_number_of_islands():
    result = number_of_islands()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
