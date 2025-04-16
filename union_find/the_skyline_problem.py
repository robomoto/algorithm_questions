import pytest

def the_skyline_problem():
    """
    You are given a list of buildings — each building is a triplet:
    [left, right, height]

    Return the skyline formed by these buildings, as a list of key points:
    [x, height]

    A key point is where the height of the skyline changes.
    """
    pass

def test_the_skyline_problem():
    result = the_skyline_problem()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
