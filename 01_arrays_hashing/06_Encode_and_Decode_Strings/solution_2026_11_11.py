"""
============================================================
Blind 75 — Encode and Decode Strings
Pattern: Arrays & Hashing
Difficulty: Medium
============================================================

PROBLEM
-------
Design an algorithm to encode a list of strings into a single
string and decode that string back into the original list.

Implement two functions:

1. encode(strs):
   Convert a list of strings into one encoded string.

2. decode(s):
   Convert the encoded string back into the original list
   of strings.

The decoded list must exactly match the original list,
including the order and contents of every string.


EXAMPLES
--------
Example 1:
    Input:  ["hello", "world"]
    Encode: "5#hello5#world"
    Decode: ["hello", "world"]

Example 2:
    Input:  ["we", "say", ":", "yes"]
    Decode: ["we", "say", ":", "yes"]

Example 3:
    Input:  ["", "hello", ""]
    Decode: ["", "hello", ""]

Example 4:
    Input:  ["hello#world", "test"]
    Decode: ["hello#world", "test"]


CONSTRAINTS
-----------
- 0 <= len(strs) <= 100
- 0 <= len(strs[i]) <= 200
- strs[i] may contain any possible characters.
- Strings may contain numbers, special characters,
  delimiters, or be completely empty.
- The decoded result must preserve the original strings.


INTERVIEW GOAL
--------------
Design an encoding method that allows strings to be
recovered without ambiguity.

Try to achieve:
    Encoding: O(n)
    Decoding: O(n)

Where n represents the total number of characters
across all strings, plus encoding overhead.


HINTS
------
Do NOT look at these until you have attempted the problem.

Hint 1:
    What happens if you simply join all strings using
    a special character as a separator?

Hint 2:
    What if one of the original strings already contains
    your chosen separator?

Hint 3:
    Could you store the length of each string before
    storing the actual string?

Hint 4:
    How could you use the length information to determine
    exactly where one string ends and the next begins?


YOUR APPROACH
-------------
Before writing code, answer these questions:

1. Why is simply joining strings with a delimiter
   potentially unsafe?

2. What information must the encoded string preserve?

3. How could you identify where each string begins
   and ends?

4. What information should you extract before decoding
   the actual string?

5. How will you advance through the encoded string
   after extracting each original string?


FUNCTION REQUIREMENTS
---------------------
encode(strs: list[str]) -> str

    Accepts a list of strings.
    Returns one encoded string.

decode(s: str) -> list[str]

    Accepts an encoded string.
    Returns the original list of strings.


TEST CASES
----------
Run the functions against these cases:

1. ["hello", "world"]
   -> ["hello", "world"]

2. ["we", "say", ":", "yes"]
   -> ["we", "say", ":", "yes"]

3. ["", "hello", ""]
   -> ["", "hello", ""]

4. ["hello#world", "test"]
   -> ["hello#world", "test"]

5. ["a", "b", "c"]
   -> ["a", "b", "c"]

6. []
   -> []

7. [""]
   -> [""]

8. ["123", "4567", "89"]
   -> ["123", "4567", "89"]

9. ["#:#", "###", "##"]
   -> ["#:#", "###", "##"]

10. ["hello", "", "world", "", "again"]
    -> ["hello", "", "world", "", "again"]
"""


def encode(strs: list[str]) -> str:
    """
    Encode a list of strings into a single string.

    Args:
        strs: A list of strings.

    Returns:
        A single encoded string.
    """

    # TODO: Implement your encoding solution here.
    # TODO: Setup variable; almost always output
    encoded = ""
    # TODO: Control Flow
    for word in strs:
    # TODO: catching & return length, delimiter and word
        encoded += str(len(word)) + "#" + word
    return encoded
    # pass


def decode(s: str) -> list[str]:
    """
    Decode a single encoded string back into a list of strings.

    Args:
        s: The encoded string.

    Returns:
        The original list of strings.
    """

    # TODO: Implement your decoding solution here.
    # TODO: Setup Variables (output and counters)
    decoded = []
    i = 0
    # TODO: Flow control
    while i < len(s):
        # TODO: Find delimiter
        j = s.find("#", i)
        # TODO: Extract and convert length
        length = int(s[i:j])
        # TODO: Move past delimiter
        i = j + 1
        # TODO: Calculate eding index
        j = int(length) + i
        # TODO: Extract and append the word
        word = s[i:j]
        decoded.append(word)
        # TODO: Advance  to the next prefix
        i = j
    # TODO: Return output
    # 
    return decoded


if __name__ == "__main__":

    test_cases = [
        ["hello", "world"],
        ["we", "say", ":", "yes"],
        ["", "hello", ""],
        ["hello#world", "test"],
        ["a", "b", "c"],
        [],
        [""],
        ["123", "4567", "89"],
        ["#:#", "###", "##"],
        ["hello", "", "world", "", "again"],
    ]

    passed_count = 0
    total_count = len(test_cases)

    print("=" * 50)
    print("ENCODE AND DECODE STRINGS - TEST RESULTS")
    print("=" * 50)

    for original in test_cases:

        encoded = encode(original)
        decoded = decode(encoded)

        passed = decoded == original

        if passed:
            passed_count += 1

        status = "PASS" if passed else "FAIL"

        print(f"Original: {original}")
        print(f"Encoded:  {encoded!r}")
        print(f"Decoded:  {decoded}")
        print(f"Expected: {original}")
        print(f"Status:   {status}")
        print("-" * 50)

    print(f"\nTests passed: {passed_count}/{total_count}")

    if passed_count == total_count:
        print("ALL TESTS PASSED!")
    else:
        print(
            f"TESTS FAILED: "
            f"{total_count - passed_count} test(s) failed."
        )