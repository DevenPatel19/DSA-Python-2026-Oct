def is_anagram(s: str, t: str) -> bool:
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
        count[char] = count.get(char, 0) +1

    # TODO 4: Loop through t and decrement each character's count.
    for char in t:
        if char not in count:
            return False
            
        count[char] -= 1
        
    # TODO 5: Return True only if all counts are zero.
    return all(value == 0 for value in count.values())
    # pass



def run_tests() -> None:
    """Run the test cases for is_anagram."""

    test_cases = [
         ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aab", "abb", False),
    ("aabb", "abbb", False),
    ("", "", True),
    ("a", "a", True),
    ("a", "b", False),
    ("ab", "a", False),
    ("listen", "silent", True),
    ("aacc", "ccac", False),
    ("abc", "abc", True),
]

    for s, t, expected in test_cases:
        actual = is_anagram(s, t)
        assert actual == expected, (
            f"is_anagram({s!r}, {t!r}): "
            f"expected {expected}, got {actual}"
        )

    print(f"All {len(test_cases)} tests passed!")
    
if __name__ == "__main__":
    run_tests()