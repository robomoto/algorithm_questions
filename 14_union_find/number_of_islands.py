import pytest

def number_of_islands():
    """
    Finds the number of islands in a 2D grid.

    Given a 2D grid consisting of '1's (land) and '0's (water), the task is to count the number of islands. 
    An island is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of 
    the grid are surrounded by water.

    Args:
        grid (List[List[str]]): A 2D grid where '1' represents land and '0' represents water.

    Returns:
        int: The number of islands in the grid.
    """

    pass

def test_number_of_islands():
    result = number_of_islands()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
