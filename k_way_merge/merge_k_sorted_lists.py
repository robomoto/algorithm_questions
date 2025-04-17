import pytest

def merge_k_sorted_lists():
    """
    Merges k sorted linked lists into one sorted linked list.

    Given k sorted linked lists, the task is to merge them into a single sorted linked list. Each list is already 
    sorted in ascending order, and the goal is to merge all the lists efficiently.

    Args:
        lists (List[ListNode]): A list of k sorted linked lists.

    Returns:
        ListNode: The head node of the merged sorted linked list.
    """

    pass

def test_merge_k_sorted_lists():
    result = merge_k_sorted_lists()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
