import pytest

def longest_common_prefix():
    """
    Finds the longest common prefix among a list of strings.

    Given a list of strings, the task is to find the longest common prefix that is shared by all the strings in the list. 
    If there is no common prefix, return an empty string.

    Args:
        strs (List[str]): A list of strings to find the common prefix.

    Returns:
        str: The longest common prefix shared by all the strings, or an empty string if there is no common prefix.
    """
    pass

def test_longest_common_prefix():
    result = longest_common_prefix()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
