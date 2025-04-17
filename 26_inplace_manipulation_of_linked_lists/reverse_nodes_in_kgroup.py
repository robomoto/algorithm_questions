import pytest

def reverse_nodes_in_kgroup():
    """
    Reverses nodes in k-sized groups in a linked list.

    Given a linked list and an integer `k`, the task is to reverse the nodes in groups of `k`. If the number of nodes
    remaining is less than `k`, those nodes should remain in their original order.

    Args:
        head (ListNode): The head node of the linked list.
        k (int): The size of the groups to reverse.

    Returns:
        ListNode: The head node of the modified linked list after reversing the nodes in groups of size `k`.
    """

    pass

def test_reverse_nodes_in_kgroup():
    result = reverse_nodes_in_kgroup()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
