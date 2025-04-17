import pytest

def longest_substring_without_repeating_characters():
    """
    Finds the length of the longest substring without repeating characters.

    Given a string, the task is to find the length of the longest substring that contains no repeating characters.
    The substring can be formed by selecting consecutive characters from the string.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """

    pass

def test_longest_substring_without_repeating_characters():
    result = longest_substring_without_repeating_characters()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
