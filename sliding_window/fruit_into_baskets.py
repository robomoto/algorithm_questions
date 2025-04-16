import pytest

def fruit_into_baskets():
    """
    You are given an array fruits, where each element represents a tree bearing a type of fruit.

    You have 2 baskets, and you can only carry one type of fruit in each.

    Pick the maximum number of fruits in a row, starting from any tree, such that:

    You only ever carry 2 types of fruit at once.
    """
    
    pass

def test_fruit_into_baskets():
    result = fruit_into_baskets()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
