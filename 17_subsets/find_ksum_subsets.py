import pytest

def find_ksum_subsets():
    """
    Finds all k-sum subsets in a list of integers.

    Given a list of integers and a target sum `k`, the task is to find all unique subsets of size `k` whose sum
    equals the target value. The solution should handle duplicates and ensure each subset is returned only once.

    Args:
        nums (List[int]): A list of integers.
        k (int): The size of the subsets to find.
        target (int): The target sum for the subsets.

    Returns:
        List[List[int]]: A list of subsets of size `k` whose sum equals the target value.
    """

    pass

def test_find_ksum_subsets():
    result = find_ksum_subsets()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
