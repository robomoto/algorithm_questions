import pytest

def alien_dictionary():
    """
    Determines the order of letters in an alien language.

    Given a list of words sorted lexicographically according to the rules of an alien language, the task is to determine
    the order of the letters in the alien alphabet. The input consists of words that are sorted according to the alien language,
    and the task is to return the order of characters as a string.

    Args:
        words (List[str]): A list of words sorted lexicographically according to the alien language.

    Returns:
        str: A string representing the order of characters in the alien language, or an empty string if no valid order exists.
    """

    pass

def test_alien_dictionary():
    result = alien_dictionary()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
