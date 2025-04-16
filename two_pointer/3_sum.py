import pytest

def three_sum():
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
    i != j,
    i != k,
    j != k, and
    nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
    """
    pass

def test_three_sum():
    result = three_sum()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
