"""
Finds the maximum average of a subarray of size k.

Given an array of integers and an integer k, the task is to find the maximum average of a subarray of size k. 
The subarray can be any contiguous subarray of length k.

Args:
    nums (List[int]): A list of integers representing the array.
    k (int): The size of the subarray.

Returns:
    float: The maximum average of any subarray of size k.
"""

import pytest
import math

def maximum_average_subarray_i(nums: list[int], k: int) -> float:
    """ O(n) solution using sliding window pattern."""
    max_mean = -1 * math.inf 
    for i in range(len(nums) - k + 1): # length of array minus the size of subarray, adjust by 1 for zero indexing
        current_nums = nums[i: i+k]
        current_mean = sum(current_nums)/k
        max_mean = max(max_mean, current_mean)
    return max_mean

@pytest.mark.parametrize("nums, k, expected_output",
                         [
                            ([1,1,1,1,1,1,1,1], 3, 1.0),
                            ([1,2,3,4,5,6,7,8], 3, 7.0),
                            ([-1,-1,-1,-1,16,16,8], 3, 13.33333)
                         ]
                        )
def test_maximum_average_subarray_i(nums, k, expected_output):
    result = maximum_average_subarray_i(nums, k)
    assert result == pytest.approx(expected_output) 
    #Approx sets a tolerance for equating floating point numbers. Didn't pass until I specified 5 decimal places

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-sv']))
