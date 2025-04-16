import pytest

def contains_duplicate_ii():
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that:
    nums[i] == nums[j], and
    abs(i - j) <= k
    """
    pass

def test_contains_duplicate_ii():
    result = contains_duplicate_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
