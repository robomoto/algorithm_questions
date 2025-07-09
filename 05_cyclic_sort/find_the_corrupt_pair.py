"""
Finds the duplicate and missing numbers in an array containing numbers from 1 to n.

The array has one number duplicated and one number missing.
The task is to identify both numbers.

Args:
    nums (List[int]): A list of integers where one number is duplicated and one is missing.

Returns:
    Tuple[int, int]: A tuple containing the duplicate number and the missing number, in that order.
"""

import pytest
import random

def find_the_corrupt_pair(nums: list[int]):
  pass

sorted_list = list(range(0, 1000))
unsorted_list = sorted_list.copy()
random.seed(0)
random.shuffle(unsorted_list)

@pytest.mark.parametrize('input, expectation',
                         [
                            ([5,4,3,2,1], [1,2,3,4,5]),
                            (unsorted_list, sorted_list),
                          ]
                        )
def test_find_the_corrupt_pair(input, expectation):
    find_the_corrupt_pair(input)
    assert input == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
