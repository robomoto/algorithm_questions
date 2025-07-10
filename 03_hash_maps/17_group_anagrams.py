'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]'''

import pytest


def group_anagrams(strs: list[str]) -> list[list[str]]:
  tracker = {}
  for item in strs:
    key = str(sorted(item)) 
    if key not in tracker:
      tracker[key] = [item]
    else:
      tracker[key].append(item)
  print(list(tracker.values()))
  return list(tracker.values())

@pytest.mark.parametrize('input, expectation',
                         [
                           (["cat", "bat", "act"], [["cat", "act"], ["bat"]]),
                          ]
                        )
def test_group_anagrams(input, expectation):
  result = group_anagrams(input)
  for item in result:
    assert len(result) == len(expectation)
    assert item in expectation
  


if __name__ == '__main__':
  import sys
  sys.exit(pytest.main([__file__, "-s"]))