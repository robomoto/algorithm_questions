"""
Checks if there are duplicates within a given range in an array.

Given an integer array and an integer k, the task is to determine if there are any duplicate numbers in the array
such that the same number appears at least twice within k indices apart.

Args:
    nums (List[int]): The input array of integers.
    k (int): The maximum index difference between two duplicate numbers.

Returns:
    bool: True if there are any duplicates within k indices apart, False otherwise.
"""

import pytest

def contains_duplicate_ii(nums: list[int], k: int) -> bool:
    """
    O(n) solution using sliding window approach.  Relatively easy because the pointers are always the same distance apart.
    The hardest part is making sure your indexes are correct. 
    """
    for i in range((len(nums)-k)+1): 
        left = i
        right = i+k+1 #+1 for zero indexing
        current_values = nums[left:right]
        current_set = set(current_values)
        # print(f"current_values: {current_values}, current_set: {current_set}")
        if len(current_set) < len(current_values):
            return True
    return False


@pytest.mark.parametrize(
    "nums, k, expected", [
        ([1, 2, 3, 1], 3, True),       # Duplicate within range of k
        ([1, 0, 1, 1], 1, True),       # Duplicate exactly 1 index apart
        ([1, 2, 3, 4], 2, False),      # No duplicate within range
        ([1, 2, 3, 1, 2, 3], 2, False),# No duplicates within range of k
        ([1, 2, 3, 4, 1, 2], 3, False), # No duplicates within range of k
        ([1, 2, 3, 4, 5], 0, False),  # k=0, no duplicates possible
        ([1], 1, False),               # Single element, no duplicates
        ([1, 2, 3, 1, 2], 4, True),    # Duplicates within range of k
    ]
)
def test_contains_duplicate_ii(nums, k, expected):
    result = contains_duplicate_ii(nums, k)
    assert result == expected

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
