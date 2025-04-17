import pytest

def group_anagrams():
    """
    Groups a list of strings into anagrams.

    Given a list of strings, the task is to group the strings that are anagrams of each other into separate lists.
    Anagrams are strings that can be formed by rearranging the letters of another string.

    Args:
        strs (List[str]): A list of strings to be grouped into anagrams.

    Returns:
        List[List[str]]: A list of lists, where each inner list contains words that are anagrams of each other.
    """

    pass

def test_group_anagrams():
    result = group_anagrams()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
