import pytest

def pairs_of_songs_with_total_durations_divisible_by_60():
    """
    Finds the number of pairs of songs whose total durations are divisible by 60.

    Given a list of song durations in seconds, the task is to find the number of pairs of songs such that
    the sum of their durations is divisible by 60.

    Args:
        time (List[int]): A list of integers representing the durations of songs in seconds.

    Returns:
        int: The number of pairs of songs whose total durations are divisible by 60.
    """

    pass

def test_pairs_of_songs_with_total_durations_divisible_by_60():
    result = pairs_of_songs_with_total_durations_divisible_by_60()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
