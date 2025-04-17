import pytest

def sort_array_by_parity_ii():
    """
    Rearranges the array so that elements at even indices are even and elements at odd indices are odd.

    The input array is guaranteed to have the same number of even and odd integers.

    Args:
        nums (List[int]): The input list of integers with equal counts of even and odd numbers.

    Returns:
        List[int]: The rearranged list satisfying the parity condition.
    """
    pass

def test_sort_array_by_parity_ii():
    result = sort_array_by_parity_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
