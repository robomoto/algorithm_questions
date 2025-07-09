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
import random

def cyclic_sort(nums: list[int]) -> None:
    "O(n)"
    for i in range(len(nums)):
        while nums[i] != i:
            swap_values(nums, i, nums[i])
    return
            
def swap_values(nums: list[int], i: int, j: int) -> list[int]:
    nums[i], nums[j] = nums[j], nums[i]
    return nums

sorted_list = list(range(0, 1000))
unsorted_list = sorted_list.copy()
random.shuffle(unsorted_list)

@pytest.mark.parametrize('input, expectation',
                         [
                           (unsorted_list, sorted_list),
                          ]
                        )
def test_cyclic_sort(input, expectation):
    cyclic_sort(input)
    assert input == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
