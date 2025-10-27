import pytest

from palindrome_checker import is_palindrome


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", True),
        ("a", True),
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("No 'x' in Nixon", True),
        ("hello", False),
        ("12321", True),
        ("12 3 21", True),
        ("Not a palindrome", False),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


def test_raw_option():
    # when raw, punctuation matters
    assert is_palindrome("A man, a plan, a canal: Panama", ignore_non_alnum=True) is True
    assert is_palindrome("A man, a plan, a canal: Panama", ignore_non_alnum=False) is False
