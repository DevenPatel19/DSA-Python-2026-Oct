"""
Python Refresher — Arrays / Lists
Supplement to DSA practice, October 13, 2026.

Run: python arrays.py
Instructions:
- Complete each TODO without looking up a solution first.
- Run the tests at the bottom.
- If stuck, ask for Hint 1 rather than requesting the solution.
"""

def second_largest_distinct(nums: list[int]) -> int | None:
    """Return the second-largest DISTINCT value, or None if it doesn't exist."""
    # TODO: Handle short lists and duplicates.
    raise NotImplementedError


def remove_all_occurrences(nums: list[int], target: int) -> list[int]:
    """Return a new list containing every value except target. Do not mutate nums."""
    # TODO: Use a list operation or comprehension.
    raise NotImplementedError


def rotate_right(nums: list[int], steps: int) -> list[int]:
    """Return a new list rotated right by steps. Empty input returns []."""
    # TODO: Consider steps larger than len(nums).
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestArrays(unittest.TestCase):
        def test_second_largest(self):
            self.assertEqual(second_largest_distinct([3, 1, 4, 4, 2]), 3)
            self.assertEqual(second_largest_distinct([5, 5]), None)
            self.assertEqual(second_largest_distinct([]), None)
            self.assertEqual(second_largest_distinct([-1, -3, -2]), -2)

        def test_remove_all_occurrences(self):
            source = [1, 2, 2, 3]
            self.assertEqual(remove_all_occurrences(source, 2), [1, 3])
            self.assertEqual(source, [1, 2, 2, 3])  # original unchanged
            self.assertEqual(remove_all_occurrences([], 1), [])

        def test_rotate_right(self):
            self.assertEqual(rotate_right([1, 2, 3, 4], 1), [4, 1, 2, 3])
            self.assertEqual(rotate_right([1, 2, 3], 5), [2, 3, 1])
            self.assertEqual(rotate_right([], 3), [])
            self.assertEqual(rotate_right([1, 2], 0), [1, 2])

    unittest.main(verbosity=2)
