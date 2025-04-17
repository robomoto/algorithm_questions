import pytest

def flatten_nested_list_iterator():
    """
    Flattens a nested list of integers using an iterator.

    Given a nested list of integers, the task is to implement an iterator that allows you to iterate over 
    all the elements in the list in a flattened manner, while keeping track of the current position in the list.

    Args:
        nestedList (List[NestedInteger]): A nested list of integers, where each element is either an integer 
                                          or a nested list.

    Returns:
        int: The next integer in the flattened list when `next()` is called on the iterator.
    """

    pass

def test_flatten_nested_list_iterator():
    result = flatten_nested_list_iterator()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
