"""
Python Refresher — Stack Operations
Supplement to DSA practice, October 13, 2026.

Focus: list append/pop, underflow, and stack-based matching.
Run: python stack_operations.py
"""

def apply_stack_commands(commands: list[tuple[str, int | None]]) -> list[int]:
    """Commands are ('push', value), ('pop', None), or ('peek', None).
    Return results of pop/peek commands. Ignore pop/peek on an empty stack.
    """
    # TODO: Implement a stack and process commands in order.
    raise NotImplementedError


def remove_adjacent_duplicates(text: str) -> str:
    """Remove adjacent equal characters repeatedly using a stack."""
    # Example: 'abbaca' -> 'ca'
    # TODO: If the current char matches the stack top, pop; otherwise push.
    raise NotImplementedError


if __name__ == "__main__":
    import unittest

    class TestStackOperations(unittest.TestCase):
        def test_commands(self):
            commands = [
                ("push", 5), ("push", 8), ("peek", None),
                ("pop", None), ("pop", None), ("pop", None)
            ]
            self.assertEqual(apply_stack_commands(commands), [8, 8, 5])

        def test_adjacent_duplicates(self):
            self.assertEqual(remove_adjacent_duplicates("abbaca"), "ca")
            self.assertEqual(remove_adjacent_duplicates("azxxzy"), "ay")
            self.assertEqual(remove_adjacent_duplicates(""), "")

    unittest.main(verbosity=2)
