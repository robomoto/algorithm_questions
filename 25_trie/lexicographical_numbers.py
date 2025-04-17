import pytest

def lexicographical_numbers():
    """
    Generates a list of lexicographically sorted numbers.

    Given an integer n, the task is to return a list of numbers from 1 to n sorted in lexicographical order.
    In lexicographical order, numbers are sorted as if they are strings, i.e., comparing digits from left to right.

    Args:
        n (int): The upper limit for the list of numbers.

    Returns:
        List[int]: A list of numbers from 1 to n sorted lexicographically.
    """


    pass

def test_lexicographical_numbers():
    result = lexicographical_numbers()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
