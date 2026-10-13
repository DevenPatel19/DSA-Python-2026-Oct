"""
Python Refresher — List Methods
Supplement to DSA practice, October 13, 2026.

Focus: append vs extend, pop, remove, sort vs sorted, slicing, copying.
Run: python array_methods.py
"""

def append_or_extend_demo() -> tuple[list[int], list[int]]:
    """Return (after_append, after_extend) using [1, 2] and [3, 4]."""
    appended = [1, 2]
    extended = [1, 2]
    # TODO: Apply append to one list and extend to the other.
    # Each should use [3, 4] as the added value.
    raise NotImplementedError


def remove_first_match(nums: list[int], target: int) -> list[int]:
    """Return a copy with only the first occurrence of target removed; unchanged if absent."""
    # TODO: Copy before mutating. Consider target not being present.
    raise NotImplementedError


def sorted_by_absolute_value(nums: list[int]) -> list[int]:
    """Return a sorted copy ordered by absolute value; do not mutate nums."""
    # TODO: Use sorted(..., key=...).
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestArrayMethods(unittest.TestCase):
        def test_append_vs_extend(self):
            appended, extended = append_or_extend_demo()
            self.assertEqual(appended, [1, 2, [3, 4]])
            self.assertEqual(extended, [1, 2, 3, 4])

        def test_remove_first_match(self):
            source = [2, 1, 2, 3]
            self.assertEqual(remove_first_match(source, 2), [1, 2, 3])
            self.assertEqual(remove_first_match(source, 9), source)
            self.assertEqual(source, [2, 1, 2, 3])

        def test_sorted_by_absolute_value(self):
            source = [-5, 2, -1, 3]
            self.assertEqual(sorted_by_absolute_value(source), [-1, 2, 3, -5])
            self.assertEqual(source, [-5, 2, -1, 3])

    unittest.main(verbosity=2)
