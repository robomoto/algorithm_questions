import pytest

def replace_words():
    """
    In English, we have a concept called root, which can be followed by some other words to form another longer word.
    For example, the root "cat" can be followed by "s", "er", "alog" to form "cats", "cater", "catalog".

    Given a dictionary consisting of many roots and a sentence, replace all the successors in the sentence with the 
    root forming it. If a successor can be replaced by multiple roots, replace it with the shortest root.

    Return the sentence after the replacement.
    """

    pass

def test_replace_words():
    result = replace_words()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
