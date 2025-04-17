import pytest

def best_time_to_buy_and_sell_stock():
    """
    Finds the best time to buy and sell stock to maximize profit.

    Given a list of stock prices where the index represents the day and the value represents the price on that day,
    the task is to determine the maximum profit that can be obtained by buying on one day and selling on another 
    later day. You are only allowed to make one buy and one sell.

    Args:
        prices (List[int]): A list representing the stock prices on each day.

    Returns:
        int: The maximum profit that can be obtained. If no profit is possible, return 0.
    """

    pass

def test_best_time_to_buy_and_sell_stock():
    result = best_time_to_buy_and_sell_stock()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
