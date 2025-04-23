"""
Reverses the words in a string.

Given a string, the task is to reverse the order of words in the string. Words are separated by spaces, and 
the spaces should be preserved in the result. The reversal of words should maintain the integrity of the characters in each word.

Args:
    s (str): The input string to reverse the words in.

Returns:
    str: The string with the words reversed.
"""
import pytest

# def reverse_words_in_string(s: str) -> str:
#     "O(n) solution: reverse all letters, split by spaces into a list, and reverse each word in the list to a join together as a string"
#     s = s[::-1]
#     words = s.split(' ')
#     output_string = ""
#     for each in words:
#         output_string += each[::-1] + " "
#     return output_string[:-1]

# I could probably also solve this without reversing the string at all:
def reverse_words_in_string(s:str) -> str:
    words = s.split(sep=' ')
    return " ".join(word for word in words[::-1])


    
@pytest.mark.parametrize("s, expected", 
                         [
                             ("sam", "sam"),
                             ("sam mas", "mas sam"),
                             ("easter sunday picnic", "picnic sunday easter")

                         ])
def test_reverse_words_in_string(s, expected):
    result = reverse_words_in_string(s)
    assert result == expected

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
