import pytest

def search_suggestions_system():
    """
    Implements a search suggestion system based on a prefix.

    Given a list of products and a search query, the task is to implement a search suggestion system that 
    suggests products based on the prefix typed by the user. The suggestions should be ordered alphabetically 
    and limited to a fixed number of suggestions.

    Args:
        products (List[str]): A list of product names.
        searchWord (str): The search query entered by the user.

    Returns:
        List[List[str]]: A list of lists where each inner list contains the suggested products for each prefix typed.
    """


    pass

def test_search_suggestions_system():
    result = search_suggestions_system()
    assert result is None  # TODO: update assertion

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
