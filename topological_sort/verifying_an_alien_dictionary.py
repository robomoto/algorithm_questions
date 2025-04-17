import pytest

def verifying_an_alien_dictionary():
    """
    Verifies if a list of words is sorted according to an alien dictionary.

    Given a list of words and an alphabet order of an alien language, the task is to verify if the words are sorted
    lexicographically according to the alien dictionary. The alien dictionary provides the order of characters, and
    the words must follow this order.

    Args:
        words (List[str]): A list of words to be checked.
        order (str): A string representing the alphabet order in the alien language.

    Returns:
        bool: True if the words are sorted according to the alien dictionary, False otherwise.
    """

    pass

def test_verifying_an_alien_dictionary():
    result = verifying_an_alien_dictionary()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
