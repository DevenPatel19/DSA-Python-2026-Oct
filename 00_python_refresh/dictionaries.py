"""
Python Refresher — Dictionaries
Supplement to DSA practice, October 13, 2026.

Focus: safe lookup, membership, updates, and mapping values to indices.
Run: python dictionaries.py
"""

def get_or_zero(counts: dict[str, int], key: str) -> int:
    """Return counts[key], or 0 if the key is missing; do not mutate counts."""
    # TODO: Prefer a safe lookup method.
    raise NotImplementedError


def invert_mapping(mapping: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary with keys and values swapped. Assume values are unique."""
    # TODO: Loop through key/value pairs.
    raise NotImplementedError


def first_pair_sum_indices(nums: list[int], target: int) -> list[int] | None:
    """Return indices of the first pair encountered in one pass, or None if absent."""
    # TODO: Store previously seen values as keys and their indices as values.
    # Check for the complement before storing the current number.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestDictionaries(unittest.TestCase):
        def test_get_or_zero(self):
            counts = {"a": 2}
            self.assertEqual(get_or_zero(counts, "a"), 2)
            self.assertEqual(get_or_zero(counts, "missing"), 0)
            self.assertEqual(counts, {"a": 2})

        def test_invert_mapping(self):
            self.assertEqual(invert_mapping({"one": "1", "two": "2"}), {"1": "one", "2": "two"})
            self.assertEqual(invert_mapping({}), {})

        def test_pair_sum_indices(self):
            self.assertEqual(first_pair_sum_indices([2, 7, 11, 15], 9), [0, 1])
            self.assertEqual(first_pair_sum_indices([3, 3], 6), [0, 1])
            self.assertIsNone(first_pair_sum_indices([1, 2, 3], 10))

    unittest.main(verbosity=2)
