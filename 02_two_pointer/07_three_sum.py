"""
Finds all unique triplets in an array that sum up to a target value.

Given an array of integers, the task is to find all unique triplets in the array whose sum is equal to zero.
The solution should not include duplicate triplets in the result.

Args:
    nums (List[int]): A list of integers to find the triplets from.

Returns:
    List[List[int]]: A list of lists, where each inner list contains three integers that sum to zero.
"""

import pytest

def three_sum(nums: list[int]):
    """Two Pointer solution.  It's worth noting that a hashmap solution is a lot easier to read and deal with edge cases.  
    I would only solve this with two pointers if hash maps where expressly not allowed.
    Issues to consider: 
    - always start by sorting the array.
    - your iteration range should leave room for your low and high pointers
    - skip duplicates
    - be sure to track when low >= high to avoid erroneous triplets
    - when one solution is found at an index, you may still have low and high options to test
    """
    nums.sort()
    results = []
  
    for i in range(len(nums) - 2): # Make sure you're leaving room for the low and high pointer values
        print(f"current index {i}")
        if i > 0 and nums[i] == nums[i - 1]: # skip if we've already seen this value
            print(f"skipping index {i}")
            continue
        low = i + 1
        high = len(nums) - 1
        while low < high:
            print(f"i: {i}, nums[i]: {nums[i]}, low: {low}, nums[low]: {nums[low]}, nums[high]: {nums[high]}")
            if nums[i] + nums[low] + nums[high] < 0:
                low += 1
            elif nums[i] + nums[low] + nums[high] > 0:
                high -= 1
            elif nums[i] + nums[low] + nums[high] == 0:
                print(f"Writing indexes: {i}, {low}, {high}")
                results.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
    return results

@pytest.mark.parametrize("nums, expectation",
                        [
                            ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
                            ([1,2,3,4,5], []),
                            ([0,0,0,0], [[0,0,0]]),
                            ([-3,-2,-1,0,1,2,3], [[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,0,1]]),
                            ([-4,-2,-2,-2,0,2,2,2,4], [[-4,0,4],[-4,2,2],[-2,-2,4],[-2,0,2]])
                        ])
def test_three_sum(nums, expectation):
    result = three_sum(nums)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
