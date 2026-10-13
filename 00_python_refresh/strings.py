"""
Python Refresher — Strings
Supplement to DSA practice, October 13, 2026.

Focus: indexing, slicing, immutability, and character processing.
Run: python strings.py
"""

def reverse_words(sentence: str) -> str:
    """Reverse word order and join with single spaces. Ignore extra whitespace."""
    # Example: "  code   every day " -> "day every code"
    # TODO: split into words, reverse, and join.
    raise NotImplementedError


def is_palindrome_phrase(text: str) -> bool:
    """Case-insensitive palindrome check ignoring non-alphanumeric characters."""
    # TODO: Normalize the string, then compare it with its reverse.
    raise NotImplementedError


def longest_word_length(sentence: str) -> int:
    """Return the longest word length, or 0 if there are no words."""
    # TODO: Consider an empty or whitespace-only string.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestStrings(unittest.TestCase):
        def test_reverse_words(self):
            self.assertEqual(reverse_words("  code   every day "), "day every code")
            self.assertEqual(reverse_words(""), "")

        def test_palindrome_phrase(self):
            self.assertTrue(is_palindrome_phrase("A man, a plan, a canal: Panama!"))
            self.assertFalse(is_palindrome_phrase("hello"))
            self.assertTrue(is_palindrome_phrase(""))

        def test_longest_word_length(self):
            self.assertEqual(longest_word_length("Python makes sense"), 6)
            self.assertEqual(longest_word_length("   "), 0)

    unittest.main(verbosity=2)
