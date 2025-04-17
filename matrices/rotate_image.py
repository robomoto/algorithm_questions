import pytest

def rotate_image():
    """
    Rotates an image represented by an n x n 2D matrix by 90 degrees clockwise.

    Given an n x n 2D matrix representing an image, the task is to rotate the image by 90 degrees in-place.
    The matrix represents the image, and each element in the matrix corresponds to a pixel in the image.

    Args:
        matrix (List[List[int]]): A 2D list representing the n x n image to be rotated.

    Returns:
        None: The image is rotated in-place, and the matrix is modified.
    """

    pass

def test_rotate_image():
    result = rotate_image()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
