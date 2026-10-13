"""
Python Refresher — Dictionary Methods
Supplement to DSA practice, October 13, 2026.

Focus: get, items, values, update, pop, membership, frequency counting.
Run: python dictionary_methods.py
"""

def count_words(words: list[str]) -> dict[str, int]:
    """Return a frequency dictionary. Treat words as case-sensitive."""
    # TODO: Count repeated words with a dictionary.
    raise NotImplementedError


def merge_counts(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    """Return summed counts from both dictionaries without mutating either input."""
    # TODO: Keys may appear in one or both dictionaries.
    raise NotImplementedError


def has_same_character_counts(s: str, t: str) -> bool:
    """Return True if s and t contain the same characters with the same frequencies."""
    # TODO: Length check is a useful early exit.
    # You can use one dictionary and increment/decrement counts.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestDictionaryMethods(unittest.TestCase):
        def test_count_words(self):
            self.assertEqual(count_words(["cat", "dog", "cat"]), {"cat": 2, "dog": 1})
            self.assertEqual(count_words([]), {})

        def test_merge_counts(self):
            left, right = {"a": 2, "b": 1}, {"a": 3, "c": 4}
            self.assertEqual(merge_counts(left, right), {"a": 5, "b": 1, "c": 4})
            self.assertEqual(left, {"a": 2, "b": 1})
            self.assertEqual(right, {"a": 3, "c": 4})

        def test_same_character_counts(self):
            self.assertTrue(has_same_character_counts("anagram", "nagaram"))
            self.assertFalse(has_same_character_counts("rat", "car"))
            self.assertTrue(has_same_character_counts("", ""))

    unittest.main(verbosity=2)
