import pytest

def implement_trie_prefix_tree():
    """
    A Trie (prefix tree) is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.

    Implement the Trie class:
      - Trie() initializes the trie object.
      - void insert(word) inserts the string word into the trie.
      - bool search(word) returns true if the word is in the trie (i.e., was inserted before), and false otherwise.
      - bool startsWith(prefix) returns true if there is a previously inserted word that has the given prefix.
    """

    pass

def test_implement_trie_prefix_tree():
    result = implement_trie_prefix_tree()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
