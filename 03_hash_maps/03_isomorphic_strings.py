"""
Determines if two strings are isomorphic.

Two strings are isomorphic if the characters in one string can be mapped to the characters in the other string 
such that every character in the first string maps to a unique character in the second string, and vice versa.

Args:
    s (str): The first string.
    t (str): The second string.

Returns:
    bool: True if the strings are isomorphic, False otherwise.
"""

import pytest

def isomorphic_strings(s: str, t: str) -> bool:
    """Simplest approach, sort and compare strings. O(n log n) solution due to sorting involved"""
    s = sorted(s)
    t = sorted(t)
    return s == t

def isomorphic_strings_with_hash_map(s: str, t: str) -> bool:
    """Solution using hash map"""
    s_map = {}
    for char in s:
        if char in s_map.keys():
            s[char] += 1
        else:
            s[char] = 1 
    for char in t:
        if char not in s_map.keys() or s_map[char] == 0:
            return False
        else:
            s_map.char -= 1
    for value in s_map.values():
        if value != 0:
            return False
    return True
        

@pytest.mark.parametrize("s,t,expectation",
                         [
                             ("sam", "mas", True),
                             ("sam", "mast", False),
                         ])
def test_isomorphic_strings_with_hash_map(s, t, expectation):
    result = isomorphic_strings(s, t)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
