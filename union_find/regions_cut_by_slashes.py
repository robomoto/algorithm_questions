import pytest

def regions_cut_by_slashes():
    """
    You are given a square grid n x n, where each cell contains either:
    ' ' (a space),
    '/', or
    '\'

    Imagine drawing the slashes on the grid and counting the number of regions formed.
    Return the number of distinct regions.
    """
    pass

def test_regions_cut_by_slashes():
    result = regions_cut_by_slashes()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
