import pytest

def remove_duplicates_from_sorted_list():
    """
    Removes duplicates from a sorted linked list.

    Given a sorted linked list, the task is to remove all duplicate elements such that each element appears 
    only once in the list. The list is sorted in ascending order.

    Args:
        head (ListNode): The head node of the sorted linked list.

    Returns:
        ListNode: The modified linked list with duplicates removed.
    """

    pass

def test_remove_duplicates_from_sorted_list():
    result = remove_duplicates_from_sorted_list()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
