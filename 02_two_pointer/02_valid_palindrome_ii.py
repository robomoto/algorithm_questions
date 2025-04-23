"""
Checks if a string can be a palindrome after removing at most one character.

Given a string, the task is to determine if it can become a valid palindrome by removing at most one character.
A palindrome is a string that reads the same forward and backward.

Args:
    s (str): The input string to check.

Returns:
    bool: True if the string can become a palindrome after removing at most one character, False otherwise.
"""

import pytest

def valid_palindrome_ii(s: str) -> bool:
    has_skipped = False
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if has_skipped:
                return False
            else:
                has_skipped = True
                if s[left] == s[right - 1]:
                  right -= 1
                elif s[left + 1] == s[right]:
                  left += 1
                else: 
                  return False
        left += 1
        right -= 1
    return True

    

@pytest.mark.parametrize("s, expectation", 
                         [
                             ("aba", True),
                             ("abbca", True),
                             ("abbcca", False),
                         ])
def test_valid_palindrome_ii(s, expectation):
    result = valid_palindrome_ii(s)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
