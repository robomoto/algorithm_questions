import pytest

def matchsticks_to_square():
    """
    Determines if it is possible to form a square using all the given matchsticks.

    Each matchstick must be used exactly once, and you cannot break any matchstick.
    The goal is to partition the matchsticks into four groups with equal sums.

    Args:
        matchsticks (List[int]): A list of integers representing the lengths of the matchsticks.

    Returns:
        bool: True if the matchsticks can form a square, False otherwise.
    """

    pass

def test_matchsticks_to_square():
    result = matchsticks_to_square()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
