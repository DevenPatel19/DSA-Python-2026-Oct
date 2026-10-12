# DSA Progress Tracker

## Current Status

- **Start date:** October 8, 2026
- **Goal:** Prepare for software developer technical interviews using Blind 75
- **Language:** Python 3
- **Learning environment:** VS Code
- **Current phase:** Arrays & Hashing
- **Last session:** October 12, 2026
- **Current focus:** Spaced review of Valid Anagram and Two Sum
- **Next new problem:** Group Anagrams (#4)

## Overall Progress

- Problems attempted: 3
- Problems completed: 3
- Problems mastered: 0
- Problems awaiting review: 3
- Study sessions completed: 4

**Status note:** All three problems have working implementations with passing tests. Contains Duplicate was independently reimplemented on October 11. Valid Anagram was reconstructed with some syntax guidance on October 12. Two Sum was implemented with guided hints on October 12. All three remain in the review phase; none has met all mastery criteria yet.

## Pattern Progress

| Pattern | Progress | Status |
|---|---:|---|
| Arrays & Hashing | 3/9 | In progress |
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
| 1 | Contains Duplicate | Hash Set | Successful independent recall; spaced review pending | 2026-10-11 | 2026-10-18 |
| 2 | Valid Anagram | Frequency Counting | Working implementation; guided recall; independent recall pending | 2026-10-12 | 2026-10-15 |
| 3 | Two Sum | Hash Map | Working implementation; guided implementation; independent recall pending | 2026-10-12 | 2026-10-15 |
| 4 | Group Anagrams | Hash Map / Frequency Counting | Not started | | |
| 5 | Top K Frequent Elements | Hash Map / Heap | Not started | | |
| 6 | Product of Array Except Self | Prefix / Suffix | Not started | | |
| 7 | Valid Sudoku | Hash Set | Not started | | |
| 8 | Encode and Decode Strings | String Encoding | Not started | | |
| 9 | Longest Consecutive Sequence | Hash Set | Not started | | |

*Review dates are planned targets, not evidence that a review has occurred. Adjust them based on recall performance.*

## Patterns Learned

### Hash Set

- **Recognition cue:** Do I need to know whether I have seen a value before?
- **Use cases:** Duplicate detection, membership testing, tracking visited values.
- **Python:** `seen = set()`, `num in seen`, `seen.add(num)`.
- **Average membership lookup:** O(1).
- **Expected time for Contains Duplicate:** O(n).
- **Worst-case auxiliary space:** O(n) when storing up to n values.
- **Important detail:** Python sets silently ignore duplicate additions; check membership before adding when duplicates must be detected.

### Hash Map

- **Recognition cue:** Do I need to look up a previously seen value or associate a value with additional information?
- **Use cases:** Two Sum, frequency counting, fast lookups, mapping values to indices.
- **Python:** `seen = {}`, `seen[key] = value`, `key in seen`, `seen[key]`.
- **Two Sum strategy:** For each number, calculate its complement using `target - num`.
- **Lookup order:** Check whether the complement exists before storing the current number.
- **Reason for lookup order:** Prevents using the same array element twice.
- **Stored information:** Map each previously seen number to its index.
- **Expected time complexity:** O(n), assuming average O(1) dictionary operations.
- **Worst-case auxiliary space:** O(n), because the dictionary may store nearly all input elements.
- **Important distinction:** Return both indices, not the values themselves.
- **Implementation pattern:** Use `enumerate(nums)` to access both the index and number during iteration.

### Sorting + Adjacent Comparison

- Sorting places equal values next to each other.
- Compare `nums[i]` with `nums[i - 1]`.
- Sorting time: O(n log n).
- Adjacent scan time: O(n).
- Overall time: O(n log n).
- `list.sort()` modifies the original list and returns `None`.
- `sorted(nums)` returns a new sorted list.
- Python sorting can use additional memory.

### Frequency Counting

- **Recognition cue:** Does the problem depend on how many times each value occurs?
- **Use cases:** Anagrams, character counts, comparing element frequencies.
- **Python:** `count[char] = count.get(char, 0) + 1`
- **Dictionary equality:** `count_s == count_t` compares key-value pairs, regardless of insertion order.
- **Frequency cancellation:** Increment counts for one string and decrement for the other.
- **Validation:** `all(value == 0 for value in count.values())`
- **Time complexity:** O(n) for two strings of length n.
- **Auxiliary space:** O(k), where k is the number of distinct characters.
- **Important distinction:** A set tracks unique values; a dictionary can track their frequencies.
- **Edge case:** Equal lengths are necessary, but not sufficient, for two strings to be anagrams.

## Session Log

### October 8, 2026 — Session 1

**Problem:** Contains Duplicate

- Identified the need to track previously seen values.
- Initially considered a list, then learned why a set is better for membership checks.
- Implemented the hash-set approach.
- Explored sorting and adjacent comparisons as an alternative.
- Practiced Python indexing, `range()`, `sort()`, `==`, and early returns.
- Practiced explaining the solution and its complexity.

See `review/day_01.md`.

### October 9, 2026 — Session 2

**Problems:** Contains Duplicate (#1 review) and Valid Anagram (#2)

#### Contains Duplicate

- Reviewed the hash-set approach and check-before-add pattern.
- Explained expected O(n) time and O(n) worst-case auxiliary space.
- Compared the hash-set solution with sorting and adjacent comparisons.
- A fresh code-from-memory test was still pending after this session.

#### Valid Anagram

- Learned why a set loses character-frequency information.
- Implemented frequency counting using dictionaries.
- Practiced incrementing counts for existing and new keys.
- Learned to compare frequency dictionaries using `==`.
- Implemented two-dictionary and one-dictionary approaches.
- Used `dict.get(char, 0)` to simplify frequency initialization.
- Learned to check whether counts cancel to zero.
- Successfully ran all 11 tests for `solution_one_dict.py`.

**Outcome:** Valid Anagram's implementation passed all 11 tests. Both problems remained under review.

See `review/day_02.md`.

### October 11, 2026 — Session 3

**Problems:** Contains Duplicate (#1 review) and Valid Anagram (#2 review)

#### Contains Duplicate

- Explained why a set is appropriate for duplicate detection.
- Reimplemented the solution independently from memory.
- Passed all 5 tests in `solution_3_day.py`.
- Explained expected O(n) time and O(n) worst-case auxiliary space.
- Result: successful independent recall; later spaced review remains necessary.

#### Valid Anagram

- Recalled why frequency counting is necessary instead of a set.
- Correctly described counting characters, decrementing frequencies, and checking that all counts are zero.
- Referenced the previous implementation to remember exact Python syntax.
- Reimplemented the one-dictionary solution and passed all 11 tests.
- Explained why the two passes and final frequency check take O(n) overall.
- Result: successful, partially assisted recall; independent implementation still needs practice.

**Session outcome:** Both implementations passed their tests. Neither problem is marked mastered.

See `review/day_03.md`.

### October 12, 2026 — Session 4

**Problems:** Valid Anagram (#2 review) and Two Sum (#3)

#### Valid Anagram

- Reconstructed the one-dictionary frequency-counting approach.
- Used a length check to reject strings of different lengths.
- Incremented counts using `count.get(char, 0) + 1`.
- Decremented counts while processing the second string.
- Returned False when a character from the second string was absent from the dictionary.
- Used `all(value == 0 for value in count.values())` to verify that frequencies balanced.
- Successfully ran all 11 tests in `solution_3_day.py`.
- Explained expected O(n) time and O(k) auxiliary space, where k is the number of distinct characters.
- Result: working implementation and correct complexity explanation; some syntax guidance was needed.

#### Two Sum

- Learned the complement strategy: `target - num`.
- Used a dictionary to map previously seen numbers to their indices.
- Used `enumerate(nums)` to obtain each index and number.
- Learned to check the complement before storing the current number.
- Implemented the return of both matching indices.
- Successfully ran all 5 tests in `solution_1_day.py`.
- Explained expected O(n) time and O(n) worst-case auxiliary space.
- Result: working implementation and correct complexity explanation; guided hints were needed during implementation.

**Session outcome:** Both implementations passed their tests. The user correctly explained the underlying algorithms and complexity, but both problems still need independent recall practice before mastery.

**Next new problem:** Group Anagrams (#4).

See `review/day_04.md` for session-specific notes, if created.

## Mistake Log / Concepts to Remember

- A list membership check can take O(n); a set provides O(1) average lookup.
- Check whether a value is present before adding it to the set.
- Python sets do not raise errors for duplicate additions.
- `=` assigns a value; `==` compares values.
- `nums.sort()` modifies the list and returns `None`.
- `sorted(nums)` returns a new sorted list.
- A `return` statement exits the function immediately.
- Start an adjacent-element comparison at index 1 to avoid comparing the first element with `nums[-1]`.
- Analyze auxiliary space using worst-case additional memory.
- Avoid claiming Python sorting always uses O(1) auxiliary space.
- `count[char] += 1` requires the key to exist first; initialize missing keys or use `count.get(char, 0) + 1`.
- `count == {}` checks whether a dictionary is empty, not whether its values are zero.
- `all(value == 0 for value in count.values())` checks whether every frequency is zero.
- Equal string lengths are necessary for anagrams, but not sufficient.
- When decrementing frequencies, handle characters absent from the original string.
- A correct algorithm and passing tests do not, by themselves, establish independent recall or mastery.
- For Two Sum, calculate the complement as `target - num`.
- Check the complement before storing the current number to avoid reusing the same index.
- A dictionary mapping values to indices lets Two Sum return both positions in expected O(n) time.

## Next Study Session

### Next Session — Planned Tasks

1. Review Valid Anagram from a blank file, without looking at the previous implementation.
2. Review Two Sum from a blank file, without step-by-step hints.
3. Run the existing tests and check edge cases.
4. Explain each solution and its time and space complexity independently.
5. Begin Blind 75 #4: Group Anagrams if review goes well.
6. Keep Contains Duplicate scheduled for October 18, adjusting if needed based on recall.

## Definition of Mastery

A problem is mastered only when I can:

- [ ] Recognize the pattern without being told.
- [ ] Explain the approach before coding.
- [ ] Implement a working solution without notes or step-by-step hints.
- [ ] Test normal cases and edge cases.
- [ ] State time and space complexity accurately.
- [ ] Explain the solution aloud as if in an interview.
- [ ] Solve it again during a later review.