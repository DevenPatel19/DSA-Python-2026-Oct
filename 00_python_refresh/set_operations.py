"""
Python Refresher — Set Operations
Supplement to DSA practice, October 13, 2026.

Focus: add, discard, membership, union, intersection, difference.
Run: python set_operations.py
"""

def symmetric_difference_values(left: set[int], right: set[int]) -> set[int]:
    """Return values present in exactly one of the two sets."""
    # TODO: Use a set operator or method.
    raise NotImplementedError


def remove_if_present(values: set[str], item: str) -> set[str]:
    """Return a modified copy with item removed if present; never raise if absent."""
    # TODO: Copy the input and choose a safe removal method.
    raise NotImplementedError


def missing_values(expected: set[int], actual: set[int]) -> set[int]:
    """Return values expected but not present in actual."""
    # TODO: Use set difference.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestSetOperations(unittest.TestCase):
        def test_symmetric_difference(self):
            self.assertEqual(symmetric_difference_values({1, 2, 3}, {3, 4}), {1, 2, 4})
            self.assertEqual(symmetric_difference_values(set(), {1}), {1})

        def test_remove_if_present(self):
            original = {"a", "b"}
            self.assertEqual(remove_if_present(original, "a"), {"b"})
            self.assertEqual(remove_if_present(original, "x"), {"a", "b"})
            self.assertEqual(original, {"a", "b"})

        def test_missing_values(self):
            self.assertEqual(missing_values({1, 2, 3}, {2}), {1, 3})
            self.assertEqual(missing_values(set(), set()), set())

    unittest.main(verbosity=2)
