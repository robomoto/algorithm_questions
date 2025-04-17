import pytest

def word_search_ii():
    """
    Finds all words in a 2D board that can be formed by a given list of words.

    Given a 2D board of letters and a list of words, the task is to find all the words from the list that can be formed
    by tracing adjacent letters in the board (horizontally or vertically). Each word must be constructed from a continuous
    sequence of adjacent letters.

    Args:
        board (List[List[str]]): A 2D list representing the board of letters.
        words (List[str]): A list of words to search for in the board.

    Returns:
        List[str]: A list of words that can be formed from the board.
    """


    pass

def test_word_search_ii():
    result = word_search_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
