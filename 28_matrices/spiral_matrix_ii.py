import pytest

def spiral_matrix_ii():
    """
    Generates an n x n matrix filled with elements from 1 to n^2 in spiral order.

    Given an integer n, the task is to generate an n x n matrix filled with numbers from 1 to n^2 such that the numbers 
    are arranged in a spiral order, starting from the top-left corner and spiraling inward.

    Args:
        n (int): The size of the matrix (n x n).

    Returns:
        List[List[int]]: A 2D list representing the matrix filled in spiral order.
    """

    pass

def test_spiral_matrix_ii():
    result = spiral_matrix_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
