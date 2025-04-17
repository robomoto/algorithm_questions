import pytest

def lucky_numbers_in_a_matrix():
    """
    Finds all lucky numbers in a given matrix.

    A lucky number in a matrix is defined as an element that is the minimum in its row and the maximum in its column.

    Args:
        matrix (List[List[int]]): A 2D list representing the matrix.

    Returns:
        List[int]: A list of lucky numbers in the matrix.
    """
    pass

def test_lucky_numbers_in_a_matrix():
    result = lucky_numbers_in_a_matrix()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
