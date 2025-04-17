import pytest

def high_five():
    """
    Returns the list of students who have received the highest number of "high fives".

    Given a list of student IDs and their corresponding high five counts, the task is to find the students who
    received the most high fives and return their IDs in ascending order.

    Args:
        items (List[List[int]]): A list where each element is a pair of student ID and the number of high fives they received.

    Returns:
        List[int]: A list of student IDs who received the most high fives, sorted in ascending order.
    """
    pass

def test_high_five():
    result = high_five()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
