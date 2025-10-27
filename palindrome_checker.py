import re
from typing import Tuple


def normalize(text: str, *, keep_non_alnum: bool = False) -> str:
    """
    Normalize text for palindrome checking.)

    - If keep_non_alnum is False (default), remove all non-alphanumeric
      characters.
    - Convert to lowercase.

    Returns the normalized string.
    """
    # If input is not a string
    if not isinstance(text, str):
        # Raise TypeError
        raise TypeError("text must be a str")

    # If we are keeping non-alphanumeric characters
    if keep_non_alnum:
        # Just convert to lowercase
        return text.lower()
    # Remove non-alphanumeric characters (ASCII letters/digits)
    return re.sub(r"[^0-9A-Za-z]+", "", text).lower()


def is_palindrome(text: str, *, ignore_non_alnum: bool = True) -> bool:
    """
    Return True if text is a palindrome.

    Parameters
    - text: input string
    - ignore_non_alnum: if True (default), ignore non-alphanumeric
      characters

    Behavior is case-insensitive by default.
    """
    # Normalize the text
    norm = normalize(text, keep_non_alnum=not ignore_non_alnum)
    # Check if normalized text is the same forwards and backwards
    return norm == norm[::-1]


def analyze(text: str) -> Tuple[str, bool]:
    """
    Return (normalized_text, is_palindrome) using default rules.
    """
    # Get normalized text
    normalized = normalize(text)
    # Check if it's a palindrome
    return normalized, normalized == normalized[::-1]
