import pytest

def house_robber_ii():
    """
    Solves the House Robber II problem, where the houses are arranged in a circle.

    In this version of the problem, you cannot rob both the first and the last house since they are adjacent.
    The task is to find the maximum amount of money that can be robbed without triggering the alarm.

    Args:
        nums (List[int]): A list of integers representing the amount of money in each house.

    Returns:
        int: The maximum amount of money that can be robbed without robbing adjacent houses.
    """

    pass

def test_house_robber_ii():
    result = house_robber_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
