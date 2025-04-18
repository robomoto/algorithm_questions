"""
Finds all repeated 10-letter DNA sequences in a string.

Given a string s representing a DNA sequence, the task is to find all the 10-letter-long sequences (substrings) 
that appear more than once in the string. The sequences should be returned as a list of strings.

Args:
    s (str): The input string representing the DNA sequence.

Returns:
    List[str]: A list of 10-letter-long repeated DNA sequences in the string.
"""

import pytest

def repeated_dna_sequences(s: str) -> list[str]:
    """
    O(n) solution using sliding window approach, tracking the sequences we've seen in a separate structure.
    """
    seen = []
    output = []
    if len(s) < 10:
        return []
    for i in range(len(s)-9):
        current_string = s[i:i+10]
        if current_string in seen and current_string not in output: 
            output.append(current_string)
        else:
            seen.append(current_string)
    return output
        



@pytest.mark.parametrize("s, expected", [
    ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
    ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ("", []),
    ("ACGTACGTAC", []),
    ("AAAAAAAAAAA", ["AAAAAAAAAA"]),
    ("AGCTAGCTAGCTAGCTAGCT", ["AGCTAGCTAG", "GCTAGCTAGC", "CTAGCTAGCT", "TAGCTAGCTA"]),
])
def test_repeated_dna_sequences(s, expected):
    result = repeated_dna_sequences(s)
    assert sorted(result) == sorted(expected)

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, '-s']))
