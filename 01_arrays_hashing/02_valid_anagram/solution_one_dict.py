
"""
Blind 75 #2: Valid Anagram — One Dictionary Approach

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

Approach:
    1. If the strings have different lengths, return False.
    2. Create one frequency dictionary.
    3. Increment counts for characters in s.
    4. Decrement counts for characters in t.
    5. Check whether all counts are zero.

Complexity target:
    Time: O(n)
    Auxiliary space: O(k), where k is the number of distinct
    characters. For a fixed alphabet, this is O(1).
"""


def is_anagram_one_dict(s: str, t: str) -> bool:
    """
    Determine whether t is an anagram of s using one dictionary.

    Args:
        s: The original string.
        t: The string to compare against s.

    Returns:
        True if s and t are anagrams; otherwise, False.
    """

    # TODO 1: Return False if the strings have different lengths.
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
    return all(value == 0 for value in count.values())
    # pass


## More Pythonic
# def is_anagram_one_dict(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False

#     count = {}

#     for char in s:
#         count[char] = count.get(char, 0) + 1

#     for char in t:
#         if char not in count:
#             return False

#         count[char] -= 1

#     return all(value == 0 for value in count.values())

def run_tests() -> None:
    """Run test cases for the one-dictionary solution."""

    test_cases = [
        # Basic cases
        ("anagram", "nagaram", True),
        ("rat", "car", False),

        # Different character frequencies
        ("aab", "abb", False),
        ("aabb", "abbb", False),

        # Edge cases
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),

        # Different lengths
        ("ab", "a", False),
        ("abc", "abcd", False),

        # Repeated characters
        ("aaa", "aaa", True),
        ("listen", "silent", True),
    ]

    passed = 0

    for s, t, expected in test_cases:
        actual = is_anagram_one_dict(s, t)

        try:
            assert actual == expected, (
                f"is_anagram_one_dict({s!r}, {t!r}): "
                f"expected {expected}, got {actual}"
            )
        except AssertionError as error:
            print(f"FAIL: {error}")
        else:
            passed += 1
            print(
                f"PASS: is_anagram_one_dict({s!r}, {t!r}) "
                f"-> {actual}"
            )

    print(f"\nResults: {passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    run_tests()