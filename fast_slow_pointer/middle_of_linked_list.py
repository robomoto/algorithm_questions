import pytest

def middle_of_linked_list():
    """
    Finds the middle node of a linked list.

    The middle node is the node that is exactly in the middle of the linked list. If the linked list
    has an even number of nodes, the second middle node is returned.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The middle node of the linked list.
    """

    pass

def test_middle_of_linked_list():
    result = middle_of_linked_list()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
