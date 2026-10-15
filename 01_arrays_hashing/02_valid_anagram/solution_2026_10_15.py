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
            count[char] =1
    # TODO 4: Loop through t and decrement each character's count.
    for char in t:
        if char in count:
            count[char]-= 1
        else:
            return False
       # TODO 5: Return True only if all counts are zero.
    return all(value == 0 for value in count.values())
    # pass


def run_tests() -> None:
    """Run the test cases for is_anagram."""

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