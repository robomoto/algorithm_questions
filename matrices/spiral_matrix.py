import pytest

def spiral_matrix():
    """
    Generates an m x n matrix filled with elements from 1 to m * n in spiral order.

    Given the dimensions m and n, the task is to generate an m x n matrix filled with numbers from 1 to m * n 
    such that the numbers are arranged in a spiral order, starting from the top-left corner and spiraling inward.

    Args:
        m (int): The number of rows in the matrix.
        n (int): The number of columns in the matrix.

    Returns:
        List[List[int]]: A 2D list representing the matrix filled in spiral order.
    """

    pass

def test_spiral_matrix():
    result = spiral_matrix()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
