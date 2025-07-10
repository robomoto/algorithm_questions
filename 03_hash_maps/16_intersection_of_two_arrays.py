'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000 '''

'''Observations:
This is under the "hashmap" section, but I think it's probably easier using sets, list comprehension and ternary operations.  It looks like a 3-line function that way.

Description: 
  Converting to sets ensures that both lists are deduplicated, then you just have to iterate over one list and check if the value is in the other list in order to return a list of the intersection.  I guess sets have some hashing under the hood for searching, so maybe that counts, I guess.
'''

import pytest

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
  set1 = set(nums1)
  set2 = set(nums2)
  return [item for item in set1 if item in set2]
  

@pytest.mark.parametrize('input, expectation',
                         [
                           ([[1,2,3], [2,3,4]], [2,3]),
                           ([[1,2,3], []], []),
                           ([[], [2,3,4]], []),
                          ]
                        )
def test_intersection(input, expectation):
  result = intersection(input[0], input[1])
  for item in result:
    assert item in expectation
    assert len(result) == len(expectation)


if __name__ == '__main__':
  import sys
  sys.exit(pytest.main([__file__]))