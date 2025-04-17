import pytest

def lemonade_change():
    """
    Determines if a customer can always receive the correct change in a lemonade stand.

    Given a list of bills representing the payments made by customers in a lemonade stand, the task is to determine 
    if the lemonade stand can always provide the correct change. The stand only accepts bills of 5, 10, or 20, and 
    it starts with no change. A customer who pays with a 5-dollar bill does not require any change, while customers 
    who pay with a 10-dollar or 20-dollar bill need to be given change. The goal is to check if it is possible 
    to provide the correct change for each customer.

    Args:
        bills (List[int]): A list of integers representing the payments made by customers.

    Returns:
        bool: True if the stand can always provide correct change, False otherwise.
    """

    pass

def test_lemonade_change():
    result = lemonade_change()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
