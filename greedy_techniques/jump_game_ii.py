import pytest

def jump_game_ii():
    """
    Determines the minimum number of jumps to reach the last index in an array.

    You are given an array of non-negative integers where each element represents your maximum jump length from that position.
    The task is to find the minimum number of jumps needed to reach the last index, starting from the first index.

    Args:
        nums (List[int]): A list of integers representing the maximum jump lengths from each position.

    Returns:
        int: The minimum number of jumps required to reach the last index, or -1 if it's not possible to reach the end.
    """
    pass

def test_jump_game_ii():
    result = jump_game_ii()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
