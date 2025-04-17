import pytest

def shortest_word_distance_ii():
    """
    Implements a data structure that supports retrieving the shortest distance between two words in a list.

    After initializing with a list of words, the structure allows efficient repeated queries for the
    shortest distance (in indices) between any two given words.

    Methods:
        shortest(word1: str, word2: str) -> int:
            Returns the shortest distance between `word1` and `word2` in the list.

    Args:
        word1 (str): The first word to search for.
        word2 (str): The second word to search for.

    Returns:
        int: The shortest distance (in number of indices) between the two words.
    """

    pass

def test_shortest_word_distance_ii():
    result = shortest_word_distance_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
