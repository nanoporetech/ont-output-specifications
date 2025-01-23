import regex_utils

import pytest


def test_regex_test():
    # Should pass without issue:
    regex_utils.test_regex_with_examples("abc", "def", "[0-9]+", ["123", "456", "789"])

    with pytest.raises(AssertionError):
        regex_utils.test_regex_with_examples("abc", "def", "[0-9]+", ["abc"])

    with pytest.raises(AssertionError):
        regex_utils.test_regex_with_examples("abc", "def", "[0-9]+", [])

    with pytest.raises(AssertionError):
        regex_utils.test_regex_with_examples("abc", "def", "[0-9]+", None)

    # Ensure partial matches fail
    with pytest.raises(AssertionError):
        regex_utils.test_regex_with_examples("abc999", "[a-z]+", None)
