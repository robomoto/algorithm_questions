import pytest

def valid_word_abbreviation():
    """
    Given a non-empty string word and a string abbr that represents an abbreviation, return true if abbr is a valid abbreviation of word.

    Rules for Abbreviation:
    A number in abbr means you skip that many characters in word.
    Leading zeros are invalid in abbreviations.
    Letters in abbr must exactly match the corresponding letters in word.
    """
    pass

def test_valid_word_abbreviation():
    result = valid_word_abbreviation()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
