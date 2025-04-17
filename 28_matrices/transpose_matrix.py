import pytest

def transpose_matrix():
    """
    Transposes a given matrix.

    Given an m x n matrix, the task is to return its transpose. The transpose of a matrix is formed by swapping 
    its rows and columns, such that the element at the i-th row and j-th column is moved to the j-th row and i-th column.

    Args:
        matrix (List[List[int]]): A 2D list representing the matrix to be transposed.

    Returns:
        List[List[int]]: The transposed matrix.
    """

    pass

def test_transpose_matrix():
    result = transpose_matrix()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
