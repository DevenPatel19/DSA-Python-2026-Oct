# Week 1 — Arrays & Hashing

**Study period:** October 8–14, 2026
**Sessions completed:** 3
**Current pattern:** Arrays & Hashing
**Primary goal:** Build reliable problem-solving recall and coding fluency for technical interviews.

---

## Weekly Objectives

- Recognize when a hash set is appropriate.
- Use a dictionary to count and compare character frequencies.
- Implement solutions from memory rather than relying on notes.
- Test normal cases and edge cases.
- Explain time and auxiliary space complexity accurately.
- Establish a spaced-repetition routine.

## Problems Studied

| # | Problem | Pattern | Current Status |
|---:|---|---|---|
| 1 | Contains Duplicate | Hash Set | Successful independent recall; later review needed |
| 2 | Valid Anagram | Frequency Counting | Successful partially assisted recall; independent implementation review needed |
| 3 | Two Sum | Hash Map | Not started |

## Patterns Learned

### Hash Set — Contains Duplicate

**Recognition cue:** Do I need to know whether I've already encountered a value?

- Maintain a set of previously seen values.
- Check membership before adding a value.
- Return early when a duplicate is found.
- Expected time: O(n).
- Worst-case auxiliary space: O(n).

### Frequency Counting — Valid Anagram

**Recognition cue:** Do I need to compare how many times values or characters occur?

- Use a dictionary to count character frequencies.
- A set alone loses frequency information.
- Frequencies can be incremented and decremented using one dictionary.
- Time: O(n).
- Auxiliary space: O(k), where k is the number of distinct characters.

## Sessions Completed

### October 8 — Session 1
**Problem:** Contains Duplicate

- Learned the hash-set approach.
- Compared hash-set membership with sorting and adjacent comparisons.
- Practiced Python indexing, `range()`, `sort()`, and early returns.
- Reviewed expected time and worst-case auxiliary space.

See `day_01.md`.

### October 9 — Session 2
**Problems:** Contains Duplicate review and Valid Anagram

- Reviewed the hash-set algorithm.
- Learned why sets are insufficient for character-frequency comparisons.
- Implemented two-dictionary and one-dictionary frequency-counting approaches.
- Passed all 11 tests for the one-dictionary solution.

See `day_02.md`.

### October 11 — Session 3
**Problems:** Contains Duplicate and Valid Anagram

- Reimplemented Contains Duplicate independently and passed all 5 tests.
- Recalled the Valid Anagram algorithm but referenced an earlier implementation for syntax.
- Passed all 11 Valid Anagram tests.
- Explained why both algorithms have linear time complexity.
- Reviewed worst-case space and the distinction between successful recall and mastery.

See `day_03.md`.

## Current Weaknesses

- Rebuild implementations without consulting previous solutions.
- Distinguish hash-set membership from frequency counting.
- Explain complexity in terms of input size and auxiliary storage.
- Continue practicing interview explanations aloud.
- Strengthen Python coding fluency through repeated implementation and testing.

## Weekly Review Checklist

- [ ] Reimplement Contains Duplicate without notes during a later review.
- [ ] Reimplement Valid Anagram without notes.
- [ ] Explain both solutions aloud.
- [ ] Verify complexity and edge cases independently.
- [ ] Complete the next spaced-repetition review.
- [ ] Begin Two Sum after review work.

## End-of-Week Assessment

**Mastered problems:** 0

Both studied problems have working implementations and passing tests, but neither has completed the full mastery criteria. Successful testing demonstrates correctness for the tested cases; later independent recall is still required.

**Next priority:** Continue reviewing Contains Duplicate and Valid Anagram, then begin Blind 75 #3 — Two Sum.