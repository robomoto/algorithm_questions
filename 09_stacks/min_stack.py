import pytest
from contextlib import nullcontext as does_not_raise

class MinStack:
  '''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int get_min() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function. '''

  def __init__(self):
    self._stack: list = []
    self._min_idx: list = []
    self._length = 0
  
  def push(self, val: int) -> None:
    self._stack.append(val)
    self._length += 1
    if self._length == 1:
      self._min_idx.append(0)
    elif val < self._stack[self._min_idx[-1]]:
      self._min_idx.append(len(self._stack) - 1)
    

  def pop(self) -> int:
    try:
      if self._length == 0:
        raise IndexError("Cannot pop an empty stack.") 
      self._length -= 1
      return_val = self._stack.pop()
      # if the top of the _min_idx stack > stack length, pop that value too.
      if self._min_idx[-1] >= self._length:
        self._min_idx.pop()
      return return_val
    except IndexError as e:
      print(e)
      raise
  
  def top(self) -> int:
    return self._stack[-1]
  
  def get_min(self) -> int:
    return self._stack[self._min_idx[-1]]



@pytest.mark.parametrize("input, expectation",
                         [
                           ([1,2,3], [1,2,3]),
                           ([5,4,3], [5,4,3])
                         ])
def test_push(input, expectation):
  s = MinStack()
  for item in input:
    s.push(item)
  assert s._stack == expectation

@pytest.mark.parametrize("input, expectation",
                         [
                           ([1,2,3], [0]),
                           ([5,4,3], [0,1,2])
                         ])
def test_push_updates_min_idx(input, expectation):
  s = MinStack()
  for item in input:
    s.push(item)
  assert s._min_idx == expectation

@pytest.mark.parametrize("input, result, expectation",
                         [
                           ([1,2,3], [1,2], does_not_raise()),
                           ([5,4,3], [5,4], does_not_raise()),
                           ([], [], pytest.raises(IndexError))
                         ])
def test_pop_one_item(input, result, expectation):
  with expectation:
    s=MinStack()
    for item in input:
      s.push(item)
    s.pop()
    assert s._stack == result

@pytest.mark.parametrize("input, result, expectation",
                         [
                           ([1,2,3], 3, does_not_raise()),
                           ([5,4,3], 3, does_not_raise()),
                           ([], [], pytest.raises(IndexError))
                         ])
def test_top(input, result, expectation):
  with expectation:
    s=MinStack()
    for item in input:
      s.push(item)
    assert s.top() == result

@pytest.mark.parametrize("input, result, expectation",
                         [
                           ([1,2,3], 1, does_not_raise()),
                           ([5,-2,3,8,14,-2], -2, does_not_raise()),
                           ([], [], pytest.raises(IndexError))
                         ])
def test_get_min(input, result, expectation):
  with expectation:
    s=MinStack()
    for item in input:
      s.push(item)
    assert s.get_min() == result


if __name__ == '__main__':
  import sys

  sys.exit(pytest.main([__file__]))
