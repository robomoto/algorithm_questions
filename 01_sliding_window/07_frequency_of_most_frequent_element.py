"""
Finds the frequency of the most frequent element in an array after performing operations.

Given an array of integers and a number of allowed operations, the task is to determine the maximum frequency
of the most frequent element after applying the allowed operations. Each operation can increase an element by 1.

Args:
    nums (List[int]): A list of integers representing the elements.
    k (int): The number of allowed operations.

Returns:
    int: The maximum frequency of the most frequent element after the operations.
"""

import pytest

def frequency_of_most_frequent_element(nums: list[int], k: int) ->int:
    """
    O(!n) solution.  Sorts the numbers in descending order, so that you can continue to iterate using k values.
    Left pointer is just stepped through the entire range. Right pointer is finding the total possible values with operations.
    I think it's O(!n)) because we're iterating to the right for every index. Maybe there is a a better solution.
    """
   
    sorted_nums = sorted(nums, reverse=True)
    print(f"Sorted nums: {sorted_nums}")
    max_qt = 0
    left = 0
    i = 0
    
    left = 0
    right = 0
    for left in range(len(sorted_nums)):
        current_qt = 0
        while right < len(sorted_nums) and \
                sorted_nums[right] == sorted_nums[left]:
            current_qt += 1
            right += 1
            current_k = k
            print(f"left: {left}, right: {right}, nums: {sorted_nums[left:right]}")
            while(current_k > 0 and right < len(sorted_nums)):
                if sorted_nums[right] + k >= sorted_nums[left]:
                    current_qt += 1
                    current_k = current_k - (sorted_nums[left] - sorted_nums[right])
                    right += 1
            max_qt = max(max_qt, current_qt)
    return max_qt

@pytest.mark.parametrize("nums, k, expectation",
                         [
                             ([1,2,1,2,1,2,1,3,3,3,3,4,4,4,4], 4, 8),
                             ([1], 1, 1),
                             ([1,1,1,2], 0, 3)
                         ])
def test_frequency_of_most_frequent_element(nums, k, expectation):
    result = frequency_of_most_frequent_element(nums, k)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
