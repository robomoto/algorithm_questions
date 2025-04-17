import pytest

def remove_all_adjacent_duplicates_in_string():
    """
    Removes all adjacent duplicates in a string.

    Given a string, the task is to remove all adjacent duplicates. If there are any adjacent characters that are the same, 
    they should be removed, and the process should continue until no adjacent duplicates are left.

    Args:
        s (str): The input string.

    Returns:
        str: The string after removing all adjacent duplicates.
    """

    pass

def test_remove_all_adjacent_duplicates_in_string():
    result = remove_all_adjacent_duplicates_in_string()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
