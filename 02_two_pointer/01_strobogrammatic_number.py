"""
Checks if a number is strobogrammatic.

A strobogrammatic number is a number that looks the same when rotated 180 degrees. The valid strobogrammatic digits are 0, 1, 6, 8, and 9.
The task is to determine if a given number is strobogrammatic.

Args:
    num (str): The input number represented as a string.

Returns:
    bool: True if the number is strobogrammatic, False otherwise.
"""
from typing import Union
import pytest

def strobogrammatic_number(nums: str) -> bool:
    "O(n) solution with two pointers"
    left = 0
    right = len(nums) - 1
    while right >= left:
        if strobogrammatic_complement(nums[left]) != nums[right]:
            return False
        left += 1
        right -= 1
    return True

def strobogrammatic_complement(c: str) -> Union[None, str]:
    """Helper function to return the strobogrammatic partner of the character supplied."""
    if c in ["0", "1", "8"]:
        return c
    if c == "6":
        return "9"
    if c == "9":
        return "6"
    else:
        return False
    

@pytest.mark.parametrize("s, expectation",
                         [
                             ("1001", True),
                             ("818", True),
                             ("96", True),
                             ("616", False),
                             ("121", False),
                             ("888", True),
                             ("99", False),
                             ("969", False),
                             ("6699", True)
                         ])
def test_strobogrammatic_number(s, expectation):
    result = strobogrammatic_number(s)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
