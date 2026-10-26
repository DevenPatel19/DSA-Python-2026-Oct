"""
Blind 75 #4: Group Anagrams
Pattern: Arrays & Hashing — Grouping by Signature
Difficulty: Medium

Problem:
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Anagrams contain the same characters with the same frequencies,
but the characters may appear in a different order.

Examples:
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    Possible output:
        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]

Constraints:
    - 1 <= len(strs) <= 10^4
    - 0 <= len(strs[i]) <= 100
    - strs[i] consists of lowercase English letters.

Requirements:
    - Use a dictionary to group the anagrams.
    - Use a sorted-character tuple as the dictionary key.
    - Do not use external libraries.
    - Preserve every input word in the output.

Learning objectives:
    - Create a consistent signature for anagrams.
    - Use tuples as dictionary keys.
    - Group values under existing dictionary keys.
    - Analyze time and auxiliary space complexity.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group strings that are anagrams of one another.

    Args:
        strs: A list of strings.

    Returns:
        A list of groups containing anagrams.
    """
    # TODO 1: Create an empty dictionary named groups.
    groups = {}
    # TODO 2: Iterate through each word in strs.
    for word in strs:
        key = tuple(sorted(word))
    # TODO 3: Create a sorted-character tuple for the current word.
        if key in groups:
    # TODO 4: If the key exists, append the word to its list.
    #         Otherwise, create a new list containing the word.
            groups[key].append(word)
        else:
            groups[key] = [word]
    # TODO 5: Return the dictionary's grouped values as a list.
    return list(groups.values())


def run_tests() -> None:
    """Run the test cases for group_anagrams."""

    test_cases = [
        # Basic grouping
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),

        # All words are anagrams
        (
            ["abc", "bca", "cab"],
            [["abc", "bca", "cab"]],
        ),

        # No words are anagrams of one another
        (
            ["abc", "def", "ghi"],
            [["abc"], ["def"], ["ghi"]],
        ),

        # Repeated words
        (
            ["eat", "eat", "tea"],
            [["eat", "eat", "tea"]],
        ),

        # Single word
        (
            ["hello"],
            [["hello"]],
        ),

        # Empty string
        (
            [""],
            [[""]],
        ),

        # Multiple empty strings
        (
            ["", ""],
            [["", ""]],
        ),

        # Same letters with different frequencies
        (
            ["aab", "abb", "aba"],
            [["aab", "aba"], ["abb"]],
        ),
    ]

    passed = 0

    for strs, expected in test_cases:
        actual = group_anagrams(strs)

        # Group order and word order within groups do not matter.
        normalize = lambda groups: sorted(
            sorted(group) for group in groups
        )

        try:
            assert normalize(actual) == normalize(expected), (
                f"group_anagrams({strs!r}): "
                f"expected {expected}, got {actual}"
            )
        except AssertionError as error:
            print(f"FAIL: {error}")
        else:
            passed += 1
            print(f"PASS: group_anagrams({strs!r})")

    print(f"\nResults: {passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    run_tests()