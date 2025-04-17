import pytest

def set_matrix_zeroes():
    """
    Modifies a matrix by setting entire rows and columns to zeroes.

    Given an m x n matrix, the task is to set any row and column containing a 0 to all zeroes. This operation
    should be done in place, without using extra space for another matrix.

    Args:
        matrix (List[List[int]]): A 2D list representing the matrix to be modified.

    Returns:
        None: The matrix is modified in place.
    """

    pass

def test_set_matrix_zeroes():
    result = set_matrix_zeroes()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
