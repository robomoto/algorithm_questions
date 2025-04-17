import pytest

def super_ugly_number():
    """
    Finds the n-th super ugly number.

    A super ugly number is a number whose prime factors are from a given list of primes. The task is to find
    the n-th super ugly number, which is the smallest number that is divisible by any combination of primes 
    from the list.

    Args:
        n (int): The index of the super ugly number to find.
        primes (List[int]): A list of prime numbers.

    Returns:
        int: The n-th super ugly number.
    """
    pass

def test_super_ugly_number():
    result = super_ugly_number()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
