"""
Finds the length of the longest substring without repeating characters.

Given a string, the task is to find the length of the longest substring that contains no repeating characters.
The substring can be formed by selecting consecutive characters from the string.

Args:
    s (str): The input string.

Returns:
    int: The length of the longest substring without repeating characters.
"""

import pytest

def longest_substring_without_repeating_characters(s: str) -> int:
    """
    O(n) solution that steps through each character as the left index.  
    This could be made faster using a while loop that would let the left 
    evalue skip ahead to the last right value, but it would still reduce to O(n)
    """
    max_length = 0
    for i in range(len(s)):
        left = i
        right = i
        current_substring = ""
        # print(f"left: {left}")
        while right < len(s) and s[right] not in current_substring:
            current_substring = current_substring + s[right]
            # print(f"right: {right}, char: {s[right]}")
            # print(f"current_substring: {current_substring}")
            right += 1
        max_length = max(max_length, len(current_substring))
        # print(f"max: {max_length}")
    # print(f"return value: {max_length}")
    return max_length
   
@pytest.mark.parametrize("s, expected", 
                         [
                             ("asdfg", 5),
                             ("aasdf", 4),
                             ("aaaaa", 1),
                             ("", 0),
                             ("abcdd", 4)
                         ])
def test_longest_substring_without_repeating_characters(s, expected):
    result = longest_substring_without_repeating_characters(s)
    assert result == expected

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
