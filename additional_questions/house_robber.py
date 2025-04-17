import pytest

def house_robber():
    """
    Finds the maximum amount of money that can be robbed from houses without alerting the police.

    Given a list of non-negative integers representing the amount of money in each house, the task is to determine the 
    maximum amount of money that can be robbed. You cannot rob two adjacent houses, as that would alert the police.

    Args:
        nums (List[int]): A list of integers representing the amount of money in each house.

    Returns:
        int: The maximum amount of money that can be robbed without robbing two adjacent houses.
    """

    pass

def test_house_robber():
    result = house_robber()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
