# Day 3 — Active Recall Review

**Date:** October 11, 2026
**Focus:** Arrays & Hashing — Contains Duplicate and Valid Anagram
**Session goal:** Retrieve previously learned solutions without relying on notes, test implementations, and explain complexity.

---

# Review of Contains Duplicate

## 1. Independent recall

I recalled the hash-set approach and implemented the solution without looking at my previous implementation.

```python
def contains_duplicate(nums: list[int]) -> bool:
    """
    Determine whether nums contains any duplicate values.
    Args:
        nums: A list of integers.
    Returns:
        True if a duplicate exists, otherwise False.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

## 2. Review results

- **Data structure:** Correct — a set tracks previously encountered values.
- **Algorithm:** Correct — check membership before adding each value, return `True` when a duplicate is found, and return `False` if the loop finishes.
- **Complexity:** Correct — O(n) expected time and O(n) worst-case auxiliary space.
- **Testing:** All 5 tests passed in `solution_3_day.py`.

Test cases included:
- A duplicate appearing after several distinct values.
- No duplicates.
- A two-element list containing duplicates.
- A single-element list.
- A duplicate near the end of the list.

## 3. Important clarification

Python sets do not raise an error when a duplicate value is added. They simply retain one copy of each value. Checking `num in seen` before calling `seen.add(num)` lets the algorithm detect a duplicate and return immediately.

The worst-case auxiliary space is O(n), because the set may store almost every input value before a duplicate is found—or store every value if no duplicate exists.

## 4. Status

**Result:** Successful independent recall.

The implementation and tests demonstrate that I can reconstruct the solution without notes. However, one successful recall session is not enough to establish long-term mastery.

**Next review:** Revisit during a later spaced-repetition session.

---

# Review of Valid Anagram

## 1. Independent recall

I correctly recalled the central algorithm:

1. Reject strings with different lengths.
2. Count each character in `s` using a dictionary.
3. Decrement the corresponding counts while processing `t`.
4. Reject a character that does not exist in the dictionary.
5. Verify that all remaining counts are zero.

I implemented the one-dictionary solution, but referenced my previous implementation to remember the exact Python syntax. This was partially assisted recall rather than a completely independent implementation.

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return False

    return all(value == 0 for value in count.values())
```

## 2. Review results

- **Data structure:** Correct — a dictionary stores character frequencies.
- **Algorithm:** Correct — count characters in the first string and cancel those counts using the second string.
- **Complexity:** Correct — O(n) time and O(k) auxiliary space, where `k` is the number of distinct characters.
- **Testing:** All 11 tests passed.

Test coverage included:
- Anagrams: `anagram` / `nagaram`
- Non-anagrams: `rat` / `car`
- Different character frequencies: `aab` / `abb`
- Different lengths: `aabb` / `abbb`
- Empty strings
- Matching and mismatching single characters
- Repeated characters
- `listen` / `silent`

## 3. Important concepts

- A set cannot distinguish strings with different character frequencies when they contain the same unique characters.
- Equal string lengths are necessary but not sufficient for anagrams.
- Dictionary equality compares keys and values, not insertion order.
- The final `all(value == 0 for value in count.values())` check verifies that all character counts cancel.
- The dictionary operations take O(1) expected time per operation. The two string passes and final dictionary check are linear overall.

For an alphabet with a fixed maximum number of possible characters, the auxiliary space can be described as O(1). In the general case, use O(k).

## 4. Status

**Result:** Successful, partially assisted recall.

I remembered the frequency-counting strategy and could explain why it works. I needed to reference the earlier implementation for exact syntax, so I still need an independent code-from-memory attempt before considering the implementation fully recalled.

**Next review:** Reimplement without notes, run the tests, and explain the complexity independently.

---

# Session Summary

## Accomplishments

- Reimplemented Contains Duplicate from memory.
- Passed all 5 Contains Duplicate tests.
- Recalled the frequency-cancellation strategy for Valid Anagram.
- Reimplemented Valid Anagram with limited syntax assistance.
- Passed all 11 Valid Anagram tests.
- Explained why both algorithms run in linear time.
- Reviewed worst-case auxiliary space and dictionary/set behavior.

## Remaining work

- Complete a later spaced review of Contains Duplicate.
- Reimplement Valid Anagram without consulting an earlier solution.
- Practice explaining both solutions aloud as if in a technical interview.
- Begin Blind 75 #3: Two Sum.

## Mastery decision

Neither problem is marked mastered yet. Both require successful later review, and Valid Anagram additionally