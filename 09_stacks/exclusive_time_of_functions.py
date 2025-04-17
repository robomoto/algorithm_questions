import pytest

def exclusive_time_of_functions():
    """
    Calculates the exclusive time of functions from a log.

    Given a list of logs representing function calls and their start and end times, the task is to calculate the 
    exclusive time spent by each function. The exclusive time of a function is the time it runs minus the time 
    spent in any nested functions.

    Args:
        n (int): The number of functions.
        logs (List[str]): A list of log entries in the format "function_id:start_time" or "function_id:end_time".

    Returns:
        List[int]: A list of integers where each element represents the exclusive time spent by the corresponding function.
    """

    pass

def test_exclusive_time_of_functions():
    result = exclusive_time_of_functions()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
