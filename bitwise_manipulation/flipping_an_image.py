import pytest

def flipping_an_image():
    """
    Flips a binary matrix horizontally, then inverts it.

    To flip the image horizontally means reversing each row.
    To invert the image means replacing each 0 with 1, and each 1 with 0.

    Args:
        image (List[List[int]]): A 2D list representing a binary matrix.

    Returns:
        List[List[int]]: The transformed image after flipping and inverting.
    """

    pass

def test_flipping_an_image():
    result = flipping_an_image()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
