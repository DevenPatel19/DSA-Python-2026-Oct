# Day 04 — Arrays & Hashing Review

**Date:** October 12, 2026  
**Focus:** Spaced repetition and hash map problem-solving  
**Language:** Python 3  
**Pattern:** Arrays & Hashing

## Session Goals

- Review Valid Anagram using frequency counting.
- Practice Two Sum using a hash map.
- Explain why the chosen data structures work.
- Analyze time and auxiliary space complexity.
- Track which solutions still need independent recall.

## Problem 2 — Valid Anagram

**Technique:** Character frequency counting with one dictionary

### Core approach

1. Return `False` if the strings have different lengths.
2. Create a dictionary to track character counts.
3. Increment counts for characters in the first string.
4. Decrement counts for characters in the second string.
5. Return `False` if a character in the second string is absent from the dictionary.
6. Check that every remaining count is zero.

### Key takeaways

- Anagrams contain the same characters with the same frequencies.
- A set alone is insufficient because it does not track how many times a character occurs.
- A single dictionary can count and cancel character frequencies.
- The length check rejects impossible matches early.

### Result

- **Tests:** Historical session results included 11/11 passing.
- **Time complexity:** O(n)
- **Auxiliary space:** O(k), where k is the number of distinct characters; O(1) if the character set is fixed.
- **Assessment:** Working implementation; independent recall still needed.

## Problem 3 — Two Sum

**Technique:** Hash map of previously seen values and indices

### Core approach

For each number, calculate the complement needed to reach the target:

`complement = target - num`

1. Iterate through the list using both index and value.
2. Calculate the complement.
3. Check whether the complement is already in the dictionary.
4. If it is, return the stored index and the current index.
5. Otherwise, store the current number and its index.

### Implementation pattern

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], index]

        seen[num] = index
```

### Key takeaways

- The dictionary maps each previously seen number to its index.
- Checking before inserting prevents using the current element twice.
- A hash map avoids repeatedly searching the remaining list.
- The returned result contains indices, not the two values.

### Result

- **Tests:** Historical session test results should be checked against the test file if exact counts are needed.
- **Expected time complexity:** O(n)
- **Auxiliary space:** O(n)
- **Assessment:** Working implementation; independent recall still needed.

## End-of-Session Summary

### Practiced

- Character frequency counting with a dictionary.
- Complement lookup with a hash map.
- Returning indices from a single-pass solution.
- Explaining why the data structure supports efficient lookup.

### Reinforcement needed

- Rebuild both solutions from a blank file without hints.
- Explain each implementation line by line.
- State time and auxiliary space complexity.
- Run the test suites again during spaced review.

## Next Session — October 13

- Revisit Valid Anagram and Two Sum through active recall.
- Continue with Blind 75 #4: Group Anagrams.
- Record test results and identify any remaining guidance needed.

**Mastery status:** Not yet confirmed. Passing tests with guidance is progress, but independent recall is the next milestone.
