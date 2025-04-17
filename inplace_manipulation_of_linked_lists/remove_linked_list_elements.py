import pytest

def remove_linked_list_elements():
    """
    Removes all nodes with a given value from a linked list.

    Given a linked list and a target value, the task is to remove all nodes in the list that have the target value.
    The function should modify the list in-place.

    Args:
        head (ListNode): The head node of the linked list.
        val (int): The value to be removed from the linked list.

    Returns:
        ListNode: The modified linked list with the specified value removed.
    """

    pass

def test_remove_linked_list_elements():
    result = remove_linked_list_elements()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
