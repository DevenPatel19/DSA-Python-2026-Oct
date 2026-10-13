
"""
Blind 75 #2: Valid Anagram
Pattern: Arrays & Hashing — Frequency Counting
Difficulty: Easy

Problem:
Given two strings s and t, return True if t is an anagram of s.
Otherwise, return False.

An anagram contains exactly the same characters with the same
frequencies, but the characters may appear in a different order.

Examples:
    s = "anagram", t = "nagaram" -> True
    s = "rat",     t = "car"     -> False
    s = "aab",     t = "abb"     -> False

Constraints:
    - s and t contain lowercase English letters.
    - Both strings may be empty.

Requirements:
    - Use frequency dictionaries.
    - Do not use sorted() for this exercise.
    - Do not use external libraries.
    - Aim for O(n) time complexity.

Learning objectives:
    - Count character frequencies with dictionaries.
    - Understand why sets alone are insufficient.
    - Compare dictionaries using ==.
    - Analyze time and auxiliary space complexity.
"""


def is_anagram(s: str, t: str) -> bool:
    """
    Determine whether t is an anagram of s.

    Args:
        s: The original string.
        t: The string to compare against s.

    Returns:
        True if s and t are anagrams; otherwise, False.
    """ # TODO 1: Return False if the strings have different lengths.
    if len(s) != len(t):
        return False
        # TODO 2: Create one empty frequency dictionary.
    count = {}
        # TODO 3: Loop through s and increment each character's count.
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
        # TODO 4: Loop through t and decrement each character's count.
    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return False
       # TODO 5: Return True only if all counts are zero.
    return all(value  == 0 for value in count.values())
    # pass


def run_tests() -> None:
    """Run the test cases for is_anagram."""

    test_cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aab", "abb", False),
    ("listen", "silent", True),
    ("", "", True),
    ("a", "", False),
    ("ab", "a", False),
    ("aacc", "ccac", False),
]

    passed = 0

    for s, t, expected in test_cases:
        actual = is_anagram(s, t)

        try:
            assert actual == expected, (
                f"is_anagram({s!r}, {t!r}): "
                f"expected {expected}, got {actual}"
            )
        except AssertionError as error:
            print(f"FAIL: {error}")
        else:
            passed += 1
            print(f"PASS: is_anagram({s!r}, {t!r}) -> {actual}")

    print(f"\nResults: {passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    run_tests()