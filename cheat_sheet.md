
# Python DSA Interview Cheat Sheet

A growing reference for Python syntax, problem-solving patterns,
complexity analysis, and interview explanations.

**Study path:** Blind 75  
**Language:** Python 3  
**Current topic:** Arrays & Hashing

---

## Table of Contents

1. [Problem-Solving Checklist](#problem-solving-checklist)
2. [Big-O Complexity](#big-o-complexity)
3. [Python Essentials](#python-essentials)
4. [Pattern: Hash Set](#pattern-hash-set)
5. [Pattern: Sorting and Adjacent Comparison](#pattern-sorting-and-adjacent-comparison)
6. [Pattern: Frequency Counting](#pattern-frequency-counting)
7. [Choosing the Right Data Structure](#choosing-the-right-data-structure)
8. [Common Mistakes](#common-mistakes)
9. [Interview Explanation Template](#interview-explanation-template)
10. [Patterns to Learn Later](#patterns-to-learn-later)

---

## Problem-Solving Checklist

Before writing code:

1. **Understand:** What are the inputs and expected outputs?
2. **Clarify:** Are empty inputs, duplicates, or unusual values possible?
3. **Recognize:** What information must I track?
4. **Choose:** Which data structure or algorithm fits?
5. **Explain:** Can I describe the approach before coding?
6. **Implement:** Write the simplest correct solution.
7. **Test:** Try normal cases and edge cases.
8. **Analyze:** State time and auxiliary space complexity.
9. **Review:** Can I reproduce the solution later without notes?

---

## Big-O Complexity

Big-O describes how resource requirements grow as input size grows.

| Complexity | Name | Typical example |
|---|---|---|
| O(1) | Constant | Set membership, average case |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | One pass through a list |
| O(n log n) | Linearithmic | Efficient comparison sorting |
| O(n²) | Quadratic | Comparing every pair with nested loops |

### Time complexity

Ask: How many operations are performed as the input grows?

- One loop over `n` items: usually O(n).
- Two separate loops over `n` items: O(n) + O(n) = O(n).
- A nested loop over the same `n` items: often O(n²).
- Sorting followed by a linear scan: O(n log n) + O(n) = O(n log n).

### Auxiliary space complexity

Ask: How much additional memory does the algorithm use, excluding the input?

- A fixed number of variables: O(1).
- A set that may store every input value: O(n).
- A dictionary of distinct characters: O(k), where `k` is the number of distinct characters.

**Important:** State your assumptions. For example, frequency counting is O(1) auxiliary space if the character alphabet is fixed at 26 lowercase English letters. Otherwise, it can be O(k).

---

## Python Essentials

### Variables and comparisons

```python
x = 5       # Assignment
x == 5      # Equality comparison
x != 5      # Inequality comparison
```

### Lists and indexing

```python
nums = [10, 20, 30]

nums[0]       # First element: 10
nums[-1]      # Last element: 30
len(nums)     # Number of elements: 3

for i in range(1, len(nums)):
    print(nums[i])
```

`range(1, len(nums))` starts at index 1 and stops before `len(nums)`.

This is useful when comparing an element with its predecessor:

```python
nums[i] == nums[i - 1]
```

### Sets

```python
seen = set()

seen.add(10)
10 in seen       # True
20 in seen       # False
```

- Stores unique elements.
- Membership lookup is O(1) on average.
- Adding an element is O(1) on average.
- Storing up to `n` distinct elements requires O(n) space.

### Dictionaries

```python
count = {}

count["a"] = 1
count["a"] += 1

count.get("b", 0)  # Returns 0 if "b" is missing
```

Frequency counting shorthand:

```python
count[char] = count.get(char, 0) + 1
```

Dictionary equality compares keys and their associated values:

```python
{"a": 2, "b": 1} == {"b": 1, "a": 2}  # True
```

The order of insertion does not affect dictionary equality.

### Loops and returns

```python
for item in items:
    if condition:
        return True

return False
```

- `return` immediately exits the function.
- `break` exits the current loop.
- `continue` skips to the next loop iteration.

### Sorting

```python
nums.sort()       # Sorts the original list in place
sorted_nums = sorted(nums)  # Creates a new sorted list
```

- Comparison sorting is typically O(n log n).
- `.sort()` returns `None`.
- Python's sorting may use additional memory.

---

## Pattern: Hash Set

### Recognition cue

**Do I need to know whether I have seen a value before?**

Useful for:
- Detecting duplicates.
- Checking membership.
- Tracking visited values.
- Avoiding repeated work.

### General template

```python
seen = set()

for item in items:
    if item in seen:
        # Handle a previously seen item
        pass

    seen.add(item)
```

### Example: Contains Duplicate

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
```

**How it works:**

1. Start with an empty set.
2. Check whether the current number has already appeared.
3. If it has, return `True`.
4. Otherwise, add it to the set.
5. If the loop finishes, return `False`.

**Complexity:**

- Expected time: O(n).
- Worst-case auxiliary space: O(n).

### Alternative: Sorting and adjacent comparison

```python
def contains_duplicate_sorted(nums: list[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False
```

Sorting puts equal values next to each other.

- Overall time: O(n log n).
- `.sort()` modifies the input.
- Sorting can use additional memory.

Use the set approach when fast membership checks are the priority. Consider sorting when ordering is useful or the problem permits modifying the input.

---

## Pattern: Sorting and Adjacent Comparison

### Recognition cue

**Can sorting make related values neighbors?**

After sorting, values that meet certain conditions may become adjacent, allowing a simple linear scan.

### General template

```python
items.sort()

for i in range(1, len(items)):
    if items[i] == items[i - 1]:
        # Handle adjacent matches
        pass
```

### Complexity

- Sorting: O(n log n).
- Scan: O(n).
- Total: O(n log n).

**Trade-off:** Sorting may simplify the algorithm, but it changes the original order. Check whether the problem allows that.

---

## Pattern: Frequency Counting

### Recognition cue

**Does the problem depend on how many times each value occurs?**

Useful for:
- Anagram detection.
- Character frequencies.
- Comparing collections by occurrence counts.

### Template: Count occurrences

```python
count = {}

for item in items:
    count[item] = count.get(item, 0) + 1
```

`get(item, 0)` returns the current count or zero if the item is new.

### Example: Valid Anagram

Two strings are anagrams when their characters occur with the same frequencies.

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_count = {}
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1

    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    return s_count == t_count
```

**Why check lengths first?**

Anagrams must have the same number of characters. Different lengths allow an immediate rejection.

**Complexity:**

- Time: O(n), where each string has length `n`.
- Auxiliary space: O(k), where `k` is the number of distinct characters.

### Alternative: Frequency cancellation

Instead of building two dictionaries, increment counts for the first string and decrement them for the second.

```python
def is_anagram_one_dict(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False

        count[char] -= 1

    return all(value == 0 for value in count.values())
```

**Why check `char not in count`?**

A character appearing in `t` but not in `s` cannot be matched. Reject it immediately instead of trying to decrement a missing key.

**Why check that all values are zero?**

Matching characters cancel out. Every character must have a final count of zero.

### Set versus frequency dictionary

A set only records whether a value exists. A dictionary can record how many times it occurs.

For example:

```python
set("aab") == set("abb")  # True
```

But `"aab"` and `"abb"` are not anagrams because their character frequencies differ.

---

## Choosing the Right Data Structure

| Need | Consider | Reason |
|---|---|---|
| Track unique values | `set` | Prevents duplicates |
| Check whether a value exists | `set` | Average O(1) membership |
| Count occurrences | `dict` | Maps values to counts |
| Associate keys with values | `dict` | Key-value lookup |
| Keep values in order | `list` | Indexed sequence |
| Process items in sorted order | `sorted()` or `.sort()` | Orders values |

These are starting points, not strict rules. Choose based on the exact information the problem requires.

---

## Common Mistakes

- Using a list when repeated membership checks would be more efficient with a set.
- Adding a value to `seen` before checking whether it is already present.
- Using `=` instead of `==` in a comparison.
- Assuming equal string lengths guarantee anagrams.
- Using a set for anagram checking and losing frequency information.
- Using `count[char] += 1` before initializing a missing key.
- Checking `count == {}` when the real requirement is that every count equals zero.
- Forgetting to handle a character that is absent from the frequency dictionary.
- Claiming `.sort()` returns a sorted list; it returns `None`.
- Claiming sorting always uses O(1) auxiliary space.
- Confusing total space with auxiliary space.
- Marking a problem mastered just because the code passed tests.

---

## Interview Explanation Template

Use this structure to explain a solution aloud.

**1. Approach**

"I'll use [data structure or algorithm] because I need to [requirement]."

**2. Algorithm**

"First, I'll [step one]. For each item, I'll [step two]. If [condition], I'll [action]. Otherwise, I'll [alternative]."

**3. Correctness**

"This works because [explain why the data structure maintains the information needed to reach the correct result]."

**4. Time complexity**

"The algorithm takes O(...) time because [explain how many times the input is processed]."

**5. Auxiliary space**

"It uses O(...) additional space because [explain what extra data is stored]."

**6. Trade-offs**

"An alternative is [alternative]. It has [complexity or other trade-off], but [reason I prefer the current approach]."

---

## Patterns to Learn Later

Add details only after studying and practicing each pattern.

- [ ] Hash Map — Two Sum
- [ ] Grouping by key — Group Anagrams
- [ ] Frequency counting with heaps — Top K Frequent Elements
- [ ] Prefix and suffix products — Product of Array Except Self
- [ ] Set validation — Valid Sudoku
- [ ] String encoding — Encode and Decode Strings
- [ ] Hash Set sequence detection — Longest Consecutive Sequence
- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Stack
- [ ] Binary Search
- [ ] Linked List
- [ ] Trees
- [ ] Heap / Priority Queue
- [ ] Backtracking
- [ ] Tries
- [ ] Graphs
- [ ] Dynamic Programming
- [ ] Greedy
- [ ] Intervals

---

## Maintenance Rules

1. Add a pattern after learning it, not before.
2. Prefer reusable templates over storing every full problem solution.
3. Record mistakes that actually occur during practice.
4. Include recognition cues so patterns are easier to identify.
5. Keep complete problem solutions in their individual problem folders.
6. Update complexity notes when you discover an important assumption.
7. Periodically try to reproduce the templates from memory.