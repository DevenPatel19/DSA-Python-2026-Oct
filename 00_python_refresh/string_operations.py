"""
Python Refresher — String Operations
Supplement to DSA practice, October 13, 2026.

Focus: strip, split, join, replace, find, startswith, and immutability.
Run: python string_operations.py
"""

def normalize_spaces(text: str) -> str:
    """Trim outer whitespace and replace any internal whitespace runs with one space."""
    # TODO: split() with no argument handles runs of whitespace; join with one space.
    raise NotImplementedError


def count_vowels(text: str) -> int:
    """Count English vowels a/e/i/o/u, case-insensitively."""
    # TODO: Normalize case and count characters.
    raise NotImplementedError


def redact_word(text: str, word: str) -> str:
    """Replace every case-sensitive occurrence of word with '[REDACTED]'."""
    # TODO: Consider an empty word; decide and document a safe behavior.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestStringOperations(unittest.TestCase):
        def test_normalize_spaces(self):
            self.assertEqual(normalize_spaces("  too   much \t space "), "too much space")
            self.assertEqual(normalize_spaces(""), "")

        def test_count_vowels(self):
            self.assertEqual(count_vowels("Interview"), 4)
            self.assertEqual(count_vowels("rhythm"), 0)

        def test_redact_word(self):
            self.assertEqual(redact_word("cat scatter cat", "cat"), "[REDACTED] s[REDACTED]ter [REDACTED]")
            self.assertEqual(redact_word("keep me", "x"), "keep me")
            self.assertEqual(redact_word("abc", ""), "abc")

    unittest.main(verbosity=2)
