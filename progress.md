
# DSA Progress Tracker

## Current Status
- **Start date:** October 8, 2026
- **Goal:** Prepare for software developer technical interviews using Blind 75
- **Language:** Python 3
- **Learning environment:** VS Code
- **Current phase:** Arrays & Hashing
- **Last session:** October 9, 2026
- **Current focus:** Review Contains Duplicate and Valid Anagram through active recall
- **Next new problem:** Two Sum (#3)

## Overall Progress

- Problems attempted: 2
- Problems completed: 2
- Problems mastered: 0
- Problems awaiting review: 2
- Study sessions completed: 2

## Pattern Progress

| Pattern | Progress | Status |
|---|---:|---|
| Arrays & Hashing | 1/9 | In progress |
| Two Pointers | 0/5 | Not started |
| Sliding Window | 0/6 | Not started |
| Stack | 0/7 | Not started |
| Binary Search | 0/7 | Not started |
| Linked List | 0/6 | Not started |
| Trees | 0/14 | Not started |
| Heap / Priority Queue | 0/2 | Not started |
| Backtracking | 0/2 | Not started |
| Tries | 0/3 | Not started |
| Graphs | 0/6 | Not started |
| Dynamic Programming | 0/12 | Not started |
| Greedy | 0/2 | Not started |
| Intervals | 0/2 | Not started |

*Pattern totals are a study roadmap and can vary by Blind 75 categorization.*

## Problem Tracker

| # | Problem | Pattern | Status | Last Attempt | Next Review |
|---:|---|---|---|---|---|
| 1 | Contains Duplicate | Hash Set | Recall in progress | 2026-10-09 | 2026-10-10 |
| 2 | Valid Anagram | Frequency Counting | Completed — review pending | 2026-10-09 | 2026-10-10 |
| 3 | Two Sum | Hash Map | Not started | | |
| 4 | Group Anagrams | Hash Map | Not started | | |
| 5 | Top K Frequent Elements | Hash Map / Heap | Not started | | |
| 6 | Product of Array Except Self | Prefix / Suffix | Not started | | |
| 7 | Valid Sudoku | Hash Set | Not started | | |
| 8 | Encode and Decode Strings | String Encoding | Not started | | |
| 9 | Longest Consecutive Sequence | Hash Set | Not started | | |

## Patterns Learned

### Hash Set

- **Recognition cue:** Do I need to know whether I have seen a value before?
- **Use cases:** Duplicate detection, membership testing, tracking visited values.
- **Python:** `seen = set()`, `num in seen`, `seen.add(num)`.
- **Average membership lookup:** O(1).
- **Worst-case auxiliary space:** O(n) when storing up to n values.

### Sorting + Adjacent Comparison

- Sorting places equal values next to each other.
- Compare `nums[i]` with `nums[i - 1]`.
- Sorting time: O(n log n).
- Adjacent scan time: O(n).
- Overall time: O(n log n).
- `list.sort()` modifies the original list.
- Python sorting can use additional memory.

### Frequency Counting

- **Recognition cue:** Does the problem depend on how many times each value occurs?
- **Use cases:** Anagrams, character counts, and comparing element frequencies.
- **Python:** `count[char] = count.get(char, 0) + 1`
- **Dictionary equality:** `count_s == count_t` compares key-value pairs.
- **Frequency cancellation:** Increment counts for one string and decrement for the other.
- **Validation:** `all(value == 0 for value in count.values())`
- **Time complexity:** O(n) for two strings of length n.
- **Auxiliary space:** O(k), where k is the number of distinct characters.
- **Important distinction:** A set tracks unique values; a dictionary can track their frequencies.

## Session Log

### October 8, 2026 — Session 1

**Problem:** Contains Duplicate

- Identified the need to track previously seen values.
- Initially proposed a list, then learned why a set is better for membership checks.
- Implemented the hash-set approach.
- Explored sorting and adjacent comparisons as an alternative.
- Practiced Python indexing, `range()`, `sort()`, `==`, and early returns.
- Practiced explaining the solution and its complexity.


### October 9, 2026 — Session 2

**Problems:** Contains Duplicate (#1 review) and Valid Anagram (#2)

#### Contains Duplicate
- Recalled the hash-set approach and explained why sets are useful for membership checks.
- Reviewed the check-before-add pattern.
- Explained expected O(n) time and O(n) worst-case auxiliary space.
- Compared the hash-set solution with sorting and adjacent comparisons.
- Code-from-memory test remains pending.

#### Valid Anagram
- Learned why a set loses character-frequency information.
- Implemented frequency counting using dictionaries.
- Practiced incrementing counts for existing and new keys.
- Learned to compare frequency dictionaries using `==`.
- Implemented the two-dictionary solution.
- Implemented the one-dictionary frequency-cancellation solution.
- Used `dict.get(char, 0)` to simplify frequency initialization.
- Learned to check whether counts cancel to zero.
- Successfully ran all 11 test cases for `solution_one_dict.py`.

### Patterns Learned
- **Hash sets:** Efficient membership checks and duplicate detection.
- **Frequency counting:** Dictionaries preserve occurrence counts that sets discard.
- **Frequency cancellation:** Incrementing and decrementing counts can establish whether two strings are anagrams.

**Outcome:** Valid Anagram implementation passes all 11 provided tests. Both problems remain scheduled for review before being marked mastered.

**Next session:**
1. Reimplement Contains Duplicate from memory.
2. Reimplement Valid Anagram from memory.
3. Explain the time and auxiliary space complexity of both.
4. Begin Blind 75 #3: Two Sum.

## Mistake Log / Concepts to Remember

- A list membership check can take O(n); a set provides O(1) average lookup.
- Check whether a value is present before adding it to the set.
- `=` assigns a value; `==` compares values.
- `nums.sort()` modifies the list and returns `None`.
- `sorted(nums)` returns a new sorted list.
- A `return` statement exits the function immediately.
- Start an adjacent-element comparison at index 1 to avoid comparing the first element with `nums[-1]`.
- Analyze auxiliary space using the worst-case amount of additional memory.
- Avoid claiming Python sorting always uses O(1) auxiliary space.
- `count[char] += 1` requires the key to exist first; initialize missing keys or use `count.get(char, 0) + 1`.
- `count == {}` checks whether a dictionary is empty, not whether its values are zero.
- `all(value == 0 for value in count.values())` checks whether every frequency is zero.
- Equal string lengths are necessary for anagrams, but not sufficient.
- When decrementing frequencies, handle characters absent from the original string.

## Next Study Session

### October 10, 2026 — Planned Tasks

1. Reimplement Contains Duplicate from memory.
2. Reimplement Valid Anagram from memory.
3. Run tests for both solutions, including edge cases.
4. Explain each solution and its time and auxiliary space complexity.
5. Begin Blind 75 #3: Two Sum if time permits.

## Definition of Mastery

A problem is mastered only when I can:

- [ ] Recognize the pattern without being told.
- [ ] Explain the approach before coding.
- [ ] Implement a working solution without notes.
- [ ] Test normal cases and edge cases.
- [ ] State time and space complexity accurately.
- [ ] Explain the solution aloud as if in an interview.
- [ ] Solve it again during a later review.