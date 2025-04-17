import pytest

def design_hashset():
    """
    Implements a HashSet without using any built-in hash table libraries.

    Supports the following operations:
      - add(key): Inserts the value into the set.
      - remove(key): Removes the value from the set if present.
      - contains(key): Returns True if the set contains the specified value.

    Methods:
        add(key: int) -> None
        remove(key: int) -> None
        contains(key: int) -> bool

    Args:
        key (int): The integer key to be added, removed, or checked.

    Returns:
        None for add and remove operations.
        bool for contains operation.
    """

    pass

def test_design_hashset():
    result = design_hashset()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
