import pytest

def split_linked_list_in_parts():
    """
    Splits a linked list into parts of equal size.

    Given a linked list and an integer `k`, the task is to split the list into `k` parts as evenly as possible.
    If the number of nodes is less than `k`, some parts will be empty. If the number of nodes is greater than `k`,
    the extra nodes should be distributed among the parts.

    Args:
        head (ListNode): The head node of the linked list.
        k (int): The number of parts to split the linked list into.

    Returns:
        List[ListNode]: A list of the `k` parts, where each part is a linked list.
    """
    pass

def test_split_linked_list_in_parts():
    result = split_linked_list_in_parts()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
