import pytest

def swap_nodes_in_pairs():
    """
    Swaps every two adjacent nodes in a linked list.

    Given a linked list, the task is to swap every two adjacent nodes. If the number of nodes is odd, 
    the last node should remain in its original position.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The head node of the modified linked list after swapping adjacent nodes.
    """

    pass

def test_swap_nodes_in_pairs():
    result = swap_nodes_in_pairs()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
