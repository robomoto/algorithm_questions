import pytest

def reverse_linked_list():
    """
    Reverses a singly linked list.

    Given a singly linked list, the task is to reverse the list such that the head becomes the tail and the tail
    becomes the head. The list should be reversed in-place without using extra memory.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The head node of the reversed linked list.
    """

    pass

def test_reverse_linked_list():
    result = reverse_linked_list()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
