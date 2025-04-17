import pytest

def coin_change():
    """
    Calculates the minimum number of coins needed to make up a given amount.

    You are given an integer array `coins` representing different denominations and an integer `amount`.
    Return the fewest number of coins needed to make up the amount.
    If it's not possible to make up the amount, return -1.

    Args:
        coins (List[int]): A list of coin denominations.
        amount (int): The total amount to form.

    Returns:
        int: The minimum number of coins required to make up the amount, or -1 if not possible.
    """

    pass

def test_coin_change():
    result = coin_change()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
