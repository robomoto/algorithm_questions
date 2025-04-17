import pytest

def reverse_nodes_in_even_length_groups():
    """
    Reverses nodes in even-length groups in a linked list.

    Given a linked list, the task is to reverse the nodes in groups where the group length is even. 
    If a group contains an odd number of nodes, the nodes in that group should remain in their original order.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The modified linked list with nodes in even-length groups reversed.
    """

    pass

def test_reverse_nodes_in_even_length_groups():
    result = reverse_nodes_in_even_length_groups()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
