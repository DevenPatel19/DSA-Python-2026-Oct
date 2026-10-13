"""
Python Refresher — Sets
Supplement to DSA practice, October 13, 2026.

Focus: uniqueness, membership, and duplicate detection.
Run: python sets.py
"""

def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears more than once."""
    # TODO: Use a set for fast membership checks.
    raise NotImplementedError


def unique_in_original_order(items: list[str]) -> list[str]:
    """Return each value once, preserving its first appearance."""
    # TODO: A set can track seen values; a list can preserve order.
    raise NotImplementedError


def common_values(left: list[int], right: list[int]) -> set[int]:
    """Return the set of values appearing in both inputs."""
    # TODO: Convert to sets and use an appropriate set operation.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestSets(unittest.TestCase):
        def test_contains_duplicate(self):
            self.assertTrue(contains_duplicate([1, 2, 1]))
            self.assertFalse(contains_duplicate([1, 2, 3]))
            self.assertFalse(contains_duplicate([]))

        def test_unique_order(self):
            self.assertEqual(unique_in_original_order(["b", "a", "b", "c", "a"]), ["b", "a", "c"])
            self.assertEqual(unique_in_original_order([]), [])

        def test_common_values(self):
            self.assertEqual(common_values([1, 2, 2, 3], [2, 4, 3]), {2, 3})
            self.assertEqual(common_values([], [1]), set())

    unittest.main(verbosity=2)
