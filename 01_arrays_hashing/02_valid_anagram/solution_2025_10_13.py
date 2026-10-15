
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
        count[char] = count.get(char,0) + 11
        # if char in count:
        #     count[char] += 1
        # else:
        #     count[char] = 1
        # TODO 4: Loop through t and decrement each character's count.
    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return False
       # TODO 5: Return True only if all counts are zero.
    return all(value == 0 for value in count.values())
    # pass


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "") is False
    assert is_anagram("a", "b") is False
    assert is_anagram("aab", "abb") is False
    assert is_anagram("abc", "abcc") is False

    print("All Valid Anagram tests passed!")


if __name__ == "__main__":
    test_is_anagram()