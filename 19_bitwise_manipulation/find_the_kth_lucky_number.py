import pytest

def find_the_kth_lucky_number():
    """
    Finds the k-th lucky number consisting only of digits 4 and 7.

    Lucky numbers are positive integers whose decimal representation contains only the digits 4 and 7.
    They are ordered in increasing numerical order (e.g., 4, 7, 44, 47, 74, 77, ...).

    Args:
        k (int): The 1-based index of the lucky number to find.

    Returns:
        int: The k-th lucky number.
    """

    pass

def test_find_the_kth_lucky_number():
    result = find_the_kth_lucky_number()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
