import pytest

def nth_tribonacci_number():
    """
    Returns the n-th number in the Tribonacci sequence.

    The Tribonacci sequence is similar to the Fibonacci sequence, but each term is the sum of the three preceding ones,
    starting with 0, 1, and 1. The sequence is defined as:
      T(0) = 0, T(1) = 1, T(2) = 1
      T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3

    Args:
        n (int): The index in the Tribonacci sequence to retrieve.

    Returns:
        int: The n-th Tribonacci number.
    """

    pass

def test_nth_tribonacci_number():
    result = nth_tribonacci_number()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
