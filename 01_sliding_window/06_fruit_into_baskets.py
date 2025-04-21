"""
Finds the maximum number of fruits that can be collected in two baskets.

Given a list of fruits where each element represents a type of fruit, the task is to find the maximum number of fruits
that can be collected in two baskets. Each basket can hold only one type of fruit, and you can swap between fruits 
only when necessary.

Args:
    fruits (List[int]): A list of integers representing different types of fruits.

Returns:
    int: The maximum number of fruits that can be collected with two baskets.
"""

import pytest

def fruit_into_baskets(fruits: list[int]) -> int:
    """O(n) solution, fairly python-specific as we're not iterating by index. 
    This doesn't use the sliding window approach. I'm not sure that I would
    use the sliding window approach for this.  It seems like you'd want to sort
    the list in order to do that, and if you just dump quantities into a dictionary, 
    you can sort the values which would be as short or shorter than the original 
    list in all cases."""
    fruit_counts = {}
    for each in fruits:
        if each not in fruit_counts:
            fruit_counts[each] = 1
        else:
            fruit_counts[each] += 1
    fruit_count_list = sorted(fruit_counts.values(), reverse=True)
    if len(fruit_count_list.keys()) > 3:
        return sum(fruit_count_list)
    return sum(fruit_count_list[:2])

@pytest.mark.parametrize("fruits, expectation",
                         [([1,2,3,1,2,3,1,2,3,1], 7),
                          ([1,1,1,1,2,2,2,2,2,3,3,3,3,3], 10)])
def test_fruit_into_baskets(fruits, expectation):
    result = fruit_into_baskets(fruits)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
