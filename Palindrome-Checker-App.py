"""
Palindrome Checker App

Simple app that checks if input strings are palindromes.
"""

import argparse
from palindrome_checker import is_palindrome, analyze


# Main function accepting command-line arguments
def main(argv: list[str] | None = None) -> int:

    # Set up argument parser
    parser = argparse.ArgumentParser(

        # Program name
        prog="palindrome-checker",
        # Program description
        description=(
            "Check whether strings are palindromes (ignores case and "
            "non-alphanumerics by default)"
        ),
    )

    # Positional argument for input text
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to check. If omitted, reads from stdin.",
    )

    # Optional flag to keep non-alphanumeric characters
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Do not strip non-alphanumeric characters",
    )

    # Parse arguments
    args = parser.parse_args(argv)

    # Determine input text
    # If no text argument provided
    if args.text is None:
        # Interactive prompt for user input
        text = input("Enter text to check for palindrome: ")

    # If text argument provided
    else:
        # Use provided text
        text = args.text

    # Check if the text is a palindrome
    result = is_palindrome(text, ignore_non_alnum=not args.raw)
    normalized, _ = analyze(text)

    # Print results
    # Display original input
    print(f"Input: {text}")

    # Display normalized text
    print(f"Normalized: {normalized}")

    # Display reversed text if not a palindrome
    if not result:
        reversed_text = normalized[::-1]
        print(f"Reversed: {reversed_text}")

    # Display palindrome result
    print("Palindrome:", "Yes" if result else "No")
    return 0


# Run main function if executed as script
if __name__ == "__main__":
    raise SystemExit(main())
