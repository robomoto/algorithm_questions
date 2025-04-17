import pytest

def reverse_linked_list_ii():
    """
    Reverses a portion of a linked list between two given positions.

    Given a linked list and two positions `left` and `right`, the task is to reverse the nodes between these two positions
    in the list, while keeping the rest of the list intact.

    Args:
        head (ListNode): The head node of the linked list.
        left (int): The starting position of the sublist to reverse.
        right (int): The ending position of the sublist to reverse.

    Returns:
        ListNode: The head node of the modified linked list after reversing the specified portion.
    """
    pass

def test_reverse_linked_list_ii():
    result = reverse_linked_list_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
