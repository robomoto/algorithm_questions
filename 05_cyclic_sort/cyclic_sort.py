
"""
Sorts an array containing `n` distinct numbers taken from the range [0, n] or [1, n].

The algorithm places each number at its correct index by swapping elements in-place,
resulting in an O(n) time complexity and O(1) space complexity.

Args:
    nums (List[int]): The unsorted list of integers.

Returns:
    None: The input list is modified in-place to be sorted.    
"""

import pytest

def cyclic_sort(nums: list[int]) -> list[int]:
    for i in range(0, len(nums)): 
        while i != nums[i]:
            swap_indexes(nums, i, nums[i])
    return nums
    

def swap_indexes(nums: list[int], i: int, j: int) -> list[int]:
    print(f"nums: {nums}, i {i}, j {j}")
    nums[i], nums[j] = nums[j], nums[i]
    print(f"post-swap: nums: {nums}")
    return nums

 
@pytest.mark.parametrize("nums, expectation",
                         [
                             ([1,3,5,2,4,0], [0,1,2,3,4,5]),
                         ])
def test_cyclic_sort(nums, expectation):
    result = cyclic_sort(nums)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
