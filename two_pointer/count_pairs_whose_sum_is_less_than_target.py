import pytest

def count_pairs_whose_sum_is_less_than_target():
    """
    Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) such that:
    0 <= i < j < n, and
    nums[i] + nums[j] < target
    """
    pass

def test_count_pairs_whose_sum_is_less_than_target():
    result = count_pairs_whose_sum_is_less_than_target()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
