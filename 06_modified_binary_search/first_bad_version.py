import pytest

def first_bad_version():
    """
    Finds the first bad version in a range of versions.

    You are given an API that determines if a version is bad. The task is to find the first bad version
    in a given range of versions, where all versions are numbered consecutively. The first bad version is 
    the first version where the API returns that the version is bad, and all subsequent versions are also bad.

    Args:
        n (int): The total number of versions.
        isBadVersion (function): An API function that takes a version number as input and returns True if the version is bad, or False if it is not.

    Returns:
        int: The version number of the first bad version.
    """

    pass

def test_first_bad_version():
    result = first_bad_version()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
