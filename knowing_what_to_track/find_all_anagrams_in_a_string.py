import pytest

def find_all_anagrams_in_a_string():
    """
    Finds all the start indices of anagrams of a given pattern in a string.

    Given a string and a pattern, the task is to find all the starting indices of the pattern's anagrams 
    in the string. The anagrams should be exact matches, and the results should be sorted in ascending order.

    Args:
        s (str): The input string.
        p (str): The pattern whose anagrams need to be found in the string.

    Returns:
        List[int]: A list of starting indices where anagrams of the pattern appear in the string.
    """

    pass

def test_find_all_anagrams_in_a_string():
    result = find_all_anagrams_in_a_string()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
