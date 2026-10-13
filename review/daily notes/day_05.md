# Day 05 — Arrays & Hashing Review

**Date:** October 13, 2026  
**Focus:** Active recall, implementation practice, and complexity analysis  
**Language:** Python 3  
**Pattern:** Arrays & Hashing

## Session Goals

- Reconstruct earlier solutions from memory.
- Practice dictionary-based problem-solving.
- Implement Group Anagrams with a stable signature.
- Explain time and auxiliary space complexity in interview-ready language.

## Problem 2 — Valid Anagram

**Technique:** Frequency counting with one dictionary

### What I practiced

- Reject strings of different lengths immediately.
- Increment character counts for the first string.
- Decrement counts while processing the second string.
- Return `False` if a character from the second string is absent from the dictionary.
- Verify that all counts are zero.

### Result

- **Tests:** 8/8 passed
- **Time:** O(n)
- **Auxiliary space:** O(k), where k is the number of distinct characters; O(1) when the character set is fixed.
- **Assessment:** Guided recall; independent recall pending.

## Problem 3 — Two Sum

**Technique:** Hash map of previously seen values and indices

### Key reasoning

For each number, calculate `complement = target - num`. Check whether the complement has already been seen before storing the current number. This prevents matching an element with itself.

### Result

- **Tests:** 5/5 passed
- **Time:** Expected O(n)
- **Auxiliary space:** O(n)
- **Assessment:** Guided implementation; independent recall pending.

## Problem 4 — Group Anagrams

**Technique:** Grouping by sorted-character signature

### Implementation pattern

```python
groups = {}

for word in strs:
    key = tuple(sorted(word))

    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

return list(groups.values())
```

### Key takeaways

- Anagrams produce the same sorted-character tuple.
- Tuples with hashable elements can be dictionary keys; lists cannot.
- The tuple is the signature; the dictionary value is a list of original words.
- Append to `groups[key]`, not to the dictionary itself.
- Initialize a new group with `[word]`.
- Preserve every input word, including duplicates.

### Result

- **Tests:** 8/8 passed
- **Time:** O(nk log k), where n is the number of strings and k is the maximum string length.
- **Auxiliary space:** O(nk) for stored signatures and grouping structures, excluding the returned output.
- **Assessment:** Working implementation with guided hints; independent recall pending.

## End-of-Session Summary

### Completed

- Reconstructed Valid Anagram's one-dictionary approach.
- Reconstructed Two Sum's complement lookup approach.
- Implemented Group Anagrams using sorted tuple signatures.
- Passed all reported tests: Valid Anagram 8/8, Two Sum 5/5, Group Anagrams 8/8.

### Reinforcement needed

- Reconstruct all three solutions from blank files without hints.
- Explain why each data structure is appropriate.
- State complexity with the input variables defined.
- Distinguish auxiliary space from returned output.

## Next Session

Review Valid Anagram, Two Sum, and Group Anagrams through independent recall. Then continue with Blind 75 #5: Top K Frequent Elements. Do not start the next session until explicitly initiated.