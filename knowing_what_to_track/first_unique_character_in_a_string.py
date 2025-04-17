import pytest

def first_unique_character_in_a_string():
    """
    Finds the first unique character in a string.

    Given a string, the task is to find the first character that appears only once in the string.
    If no unique character exists, return -1.

    Args:
        s (str): The input string.

    Returns:
        int: The index of the first unique character, or -1 if no unique character exists.
    """

    pass

def test_first_unique_character_in_a_string():
    result = first_unique_character_in_a_string()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
