"""
Python Refresher — Queue Operations
Supplement to DSA practice, October 13, 2026.

Focus: enqueue, dequeue, peek, empty queues, and FIFO order.
Run: python queue_operations.py
"""

def run_queue_commands(commands: list[tuple[str, int | None]]) -> list[int]:
    """Commands are ('enqueue', value), ('dequeue', None), or ('peek', None).
    Return results of dequeue/peek commands. Ignore dequeue/peek on an empty queue.
    """
    # TODO: Use collections.deque.
    raise NotImplementedError


def recent_unique_values(values: list[int], window_size: int) -> list[list[int]]:
    """Return the unique values in each sliding window, preserving first appearance order.
    If window_size <= 0 or exceeds len(values), return [].
    """
    # TODO: Start with a simple correct solution; optimize only if needed.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestQueueOperations(unittest.TestCase):
        def test_commands(self):
            commands = [
                ("enqueue", 10), ("enqueue", 20), ("peek", None),
                ("dequeue", None), ("dequeue", None), ("dequeue", None)
            ]
            self.assertEqual(run_queue_commands(commands), [10, 10, 20])

        def test_recent_unique_values(self):
            self.assertEqual(recent_unique_values([1, 2, 1, 3], 3), [[1, 2], [2, 1, 3]])
            self.assertEqual(recent_unique_values([1, 2], 0), [])
            self.assertEqual(recent_unique_values([1, 2], 3), [])

    unittest.main(verbosity=2)
