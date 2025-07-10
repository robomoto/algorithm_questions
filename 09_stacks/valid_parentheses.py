import pytest

def valid_parentheses(s: str) -> bool:
  """
  Checks if a string contains valid parentheses.

  Given a string containing parentheses, the task is to determine if the parentheses are valid. A string is valid
  if the parentheses are properly balanced, meaning each opening parenthesis has a corresponding closing parenthesis,
  and the parentheses are correctly nested.

  Args:
      s (str): The input string containing parentheses.

  Returns:
      bool: True if the string contains valid parentheses, False otherwise.
  """
  _stack = []
  char_map = {
    "(": ")",
    "[": "]",
    "{": "}"
  }
  for c in s:
    if c in ["(","{","["]:
      _stack.append(c)
    elif char_map[_stack.pop()] != c:
       return False
  if len(_stack) > 0:
     return False
  return True

      
        
@pytest.mark.parametrize("input, expectation",
                         [
                           ("()", True),
                           ("{}", True),
                           ("([])", True),
                           ("[([])]", True),
                           ("{[]", False),
                           ("{[])", False),
                          ])
def test_valid_parentheses(input, expectation):
    result = valid_parentheses(input)
    assert result == expectation

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-s"]))
