"""
Python Refresher — Queues
Supplement to DSA practice, October 13, 2026.

A queue is FIFO: first in, first out. collections.deque supports efficient popleft().
Run: python queues.py
"""

def process_queue(customers: list[str], new_arrivals: list[str]) -> list[str]:
    """Serve all existing customers, then new arrivals; return serving order."""
    # TODO: Use collections.deque and popleft(), not list.pop(0).
    raise NotImplementedError


def first_unique_character(text: str) -> str | None:
    """Return the first character that occurs once, or None if none exists."""
    # TODO: Combine a frequency dictionary with original-order traversal.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestQueues(unittest.TestCase):
        def test_process_queue(self):
            self.assertEqual(process_queue(["A", "B"], ["C"]), ["A", "B", "C"])
            self.assertEqual(process_queue([], []), [])

        def test_first_unique_character(self):
            self.assertEqual(first_unique_character("leetcode"), "l")
            self.assertEqual(first_unique_character("aabb"), None)
            self.assertEqual(first_unique_character(""), None)

    unittest.main(verbosity=2)
