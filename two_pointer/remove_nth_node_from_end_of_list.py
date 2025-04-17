import pytest

def remove_nth_node_from_end_of_list():
    """
    Removes the n-th node from the end of a linked list.

    Given the head of a singly linked list, the task is to remove the n-th node from the end of the list.
    The list is 1-indexed, and the function should return the head of the modified list.

    Args:
        head (ListNode): The head node of the singly linked list.
        n (int): The position (1-based) of the node to remove from the end of the list.

    Returns:
        ListNode: The head node of the modified linked list.
    """

    pass

def test_remove_nth_node_from_end_of_list():
    result = remove_nth_node_from_end_of_list()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
