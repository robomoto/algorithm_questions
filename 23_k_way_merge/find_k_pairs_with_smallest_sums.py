import pytest

def find_k_pairs_with_smallest_sums():
    """
    Finds the k pairs with the smallest sums from two lists.

    Given two lists of integers, the task is to find the k pairs (one element from each list) with the smallest sums.
    The pairs should be sorted by their sum in ascending order.

    Args:
        nums1 (List[int]): The first list of integers.
        nums2 (List[int]): The second list of integers.
        k (int): The number of pairs to return.

    Returns:
        List[Tuple[int, int]]: A list of k pairs with the smallest sums.
    """

    pass

def test_find_k_pairs_with_smallest_sums():
    result = find_k_pairs_with_smallest_sums()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
