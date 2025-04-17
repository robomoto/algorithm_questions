import pytest

def letter_case_permutation():
    """
    Generates all possible permutations of a string with letter case changes.

    Given a string, the task is to generate all possible permutations of the string where each letter can be
    either lowercase or uppercase. Non-alphabetical characters should remain unchanged.

    Args:
        s (str): The input string consisting of letters and potentially other characters.

    Returns:
        List[str]: A list of all possible permutations of the string with letter case variations.
    """

    pass

def test_letter_case_permutation():
    result = letter_case_permutation()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
