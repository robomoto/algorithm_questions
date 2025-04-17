import pytest

def reorder_list():
    """
    Reorders a linked list in a specific pattern.

    Given a singly linked list, the task is to reorder the list such that the nodes alternate between
    the first and the last nodes, then the second and second last nodes, and so on. This reordering
    should be done in-place.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The reordered linked list.
    """

    pass

def test_reorder_list():
    result = reorder_list()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
