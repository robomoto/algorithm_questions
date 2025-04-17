import pytest

def fraction_to_recurring_decimal():
    """
    Converts a fraction to a recurring decimal.

    Given a numerator and a denominator, the task is to return the fraction as a decimal string. If the decimal is
    recurring, it should be enclosed in parentheses. If there is no recurring part, the decimal is returned as a finite number.

    Args:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.

    Returns:
        str: The decimal representation of the fraction, with recurring decimals in parentheses if applicable.
    """
    pass

def test_fraction_to_recurring_decimal():
    result = fraction_to_recurring_decimal()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
