import pytest

def find_the_longest_substring_having_vowels_in_even_counts():
    """
    Finds the length of the longest substring in which each of the vowels
    ('a', 'e', 'i', 'o', 'u') appears an even number of times.

    The substring must be contiguous, and the input is assumed to consist of only
    lowercase English letters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest valid substring with even vowel counts.
    """

    pass

def test_find_the_longest_substring_having_vowels_in_even_counts():
    result = find_the_longest_substring_having_vowels_in_even_counts()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
