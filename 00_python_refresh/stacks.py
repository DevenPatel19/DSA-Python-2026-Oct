"""
Python Refresher — Stacks
Supplement to DSA practice, October 13, 2026.

A stack is LIFO: last in, first out. Python lists work well for stack ends.
Run: python stacks.py
"""

def reverse_with_stack(items: list[str]) -> list[str]:
    """Return a reversed copy by pushing then popping items."""
    # TODO: Use append() to push and pop() to remove from the top.
    raise NotImplementedError


def is_balanced_brackets(text: str) -> bool:
    """Check (), [], and {} bracket pairs; ignore all non-bracket characters."""
    # TODO: Push opening brackets and validate each closing bracket.
    raise NotImplementedError


def next_greater_values(nums: list[int]) -> list[int]:
    """For each number, return the first greater value to its right, or -1 if none."""
    # TODO: Use a monotonic stack of indices or values.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestStacks(unittest.TestCase):
        def test_reverse_with_stack(self):
            self.assertEqual(reverse_with_stack(["a", "b", "c"]), ["c", "b", "a"])
            self.assertEqual(reverse_with_stack([]), [])

        def test_balanced_brackets(self):
            self.assertTrue(is_balanced_brackets("f(a[0] + {b})"))
            self.assertFalse(is_balanced_brackets("([)]"))
            self.assertFalse(is_balanced_brackets("((("))
            self.assertTrue(is_balanced_brackets("no brackets"))

        def test_next_greater_values(self):
            self.assertEqual(next_greater_values([2, 1, 3]), [3, 3, -1])
            self.assertEqual(next_greater_values([4, 3, 2]), [-1, -1, -1])
            self.assertEqual(next_greater_values([]), [])

    unittest.main(verbosity=2)
