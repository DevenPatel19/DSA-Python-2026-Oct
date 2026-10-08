# DSA Roadmap

## How we'll learn
For each problem, we'll work through the same interview workflow:

01. Recognize the pattern
02. Understand the data structure
03. Work through a brute-force approach
04. Identify why it is too slow / awkward
05. Derive the optimal approach
06. Implement it together in Python
07. Dry-run it
08. Discuss edge cases
09. Explain it out loud like an interview
10. Do a follow-up variation
11. Revisit it later using spaced repetition


## The Blind 75 pattern roadmap

I'd use roughly this progression:
'''
                    DSA INTERVIEW ROADMAP
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
    DATA STRUCTURES                    ALGORITHMIC PATTERNS
          │                                   │
    Arrays / Strings                    Two Pointers
    Hash Maps/Sets                      Sliding Window
    Linked Lists                        Binary Search
    Stacks / Queues                     Prefix / Running State
    Trees                               Intervals
    Heaps                               Stack Patterns
    Graphs                              Fast / Slow Pointers
    Tries                               DFS / BFS
    Union-Find                          Backtracking
                                        Dynamic Programming
                                        Greedy
                                        Topological Sort
                                        Graph Algorithms

'''

The important thing is that patterns are more valuable than individual problems.

For example, these aren't really five completely different problems:

'''
Two Sum
3Sum
4Sum
Two Sum II
Subarray problems
'''

They teach variations of:

How can I avoid repeatedly searching for something I could remember?

That leads you toward hashing, sorting, and two-pointer techniques.

## Your VS Code learning environment

I recommend making a dedicated repository rather than throwing everything into one folder.

This structure is intentional.

You want to eventually be able to open VS Code and think:

"I have 45 minutes. What should I practice?"

and immediately know where to go.

## Every problem gets the same format

For example:
'''
01_arrays_hashing/
└── 03_two_sum/
    ├── problem.md
    ├── solution.py
    └── notes.md
'''

### problem.md
'''
# Two Sum

## Pattern
Hash Map

## Difficulty
Easy

## Problem

Given an array of integers `nums` and an integer `target`,
return the indices of the two numbers such that they add up
to `target`.

You may assume that each input has exactly one solution.

## Examples

Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

## Constraints

- Each input has exactly one solution.
- You may not use the same element twice.

## Interview Goal

Solve this in O(n) time.

'''

### solution.py
Initially:
'''
def two_sum(nums: list[int], target: int) -> list[int]:
    pass
'''

Do not put the answer in immediately.

This is your interview simulation.

After solving it, you can write:

'''
def two_sum(nums: list[int], target: int) -> list[int]:
    ...
'''

Then add tests:

'''
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
'''

### notes.md
'''
# Two Sum — Notes

## Pattern

Hash Map

## Key Insight

Instead of searching the rest of the array for the complement,
store numbers we have already seen.

For each number:

complement = target - number

Then check whether complement is already in the hash map.

## Why It Works

...

## Common Mistake

Trying every pair with nested loops.

## Interview Explanation

...

## Similar Problems

- 3Sum
- Two Sum II
- 4Sum

## Review

- [ ] First attempt
- [ ] Solved without hints
- [ ] Solved again from memory
- [ ] Explained aloud
- [ ] Reviewed after 1 day
- [ ] Reviewed after 1 week
- [ ] Reviewed after 1 month
'''

## Your master progress tracker

we'll maintain somthing like this:

'''
        # DSA Progress

        ## Legend

        🟢 Can solve independently
        🟡 Need a hint
        🔴 Cannot solve yet
        🔵 Reviewed

        ---

        ## Arrays & Hashing

        | Problem | Status | Pattern | Last Review |
        |---|---|---|---|
        | Contains Duplicate | 🔴 | Hash Set | |
        | Valid Anagram | 🔴 | Hash Map | |
        | Two Sum | 🔴 | Hash Map | |
        | Group Anagrams | 🔴 | Hash Map | |
        | Top K Frequent Elements | 🔴 | Hash Map + Heap | |
        | Product of Array Except Self | 🔴 | Prefix/Suffix | |
        | Valid Sudoku | 🔴 | Hash Set | |
        | Encode and Decode Strings | 🔴 | String | |
        | Longest Consecutive Sequence | 🔴 | Hash Set | |

        ---

        ## Two Pointers

        | Problem | Status | Pattern | Last Review |
        |---|---|---|---|
        | Valid Palindrome | 🔴 | Two Pointer | |
        | Two Sum II | 🔴 | Two Pointer | |
        | 3Sum | 🔴 | Two Pointer | |
        | Container With Most Water | 🔴 | Two Pointer | |
        | Trapping Rain Water | 🔴 | Two Pointer | |

'''
## Your daily practice system

Since our biggest problem is "getting cold" or "skill atrophy", I don't want to study DSA only when I have
and ainterview

Instead:

Minimum day — 30 minutes
    10 min → review yesterday's problem

    15 min → solve one problem

    5 min → write what you learned

Normal day — 60 minutes
    10 min → spaced review

    30 min → new problem

    10 min → explain solution aloud

    10 min → notes / mistake log

Deep-study day — 90–120 minutes
    15 min → review

    45 min → new problem

    20 min → implementation from scratch

    15 min → variation

    15 min → interview explanation

The 30-minute minimum matters.

If you're busy, don't abandon DSA completely.

Keeping the mental machinery warm is the point.

## 7. The most important habit: don't look at solutions too quickly

We'll use a hint ladder.

Suppose you get:

Given an array, find two numbers that add to a target.

You shouldn't immediately see:

seen = {}

Instead I'll ask:

Hint 1

What information would be useful to remember while traversing the array?

If you're stuck:

Hint 2

For each number x, what other number would you need?

Then:

Hint 3

target - x

Then:

Hint 4

What Python data structure gives you approximately constant-time lookup?

Then finally:

Hint 5

Use a hash map.

This process builds problem-solving intuition, rather than solution memorization.

## 8. Your interview thought process

Eventually I want you to automatically go through this checklist.

When I give you:

"Given an array..."

your brain should start asking:

ARRAY
 │
 ├── Need lookup?
 │      └── Hash Map / Set
 │
 ├── Sorted?
 │      └── Binary Search / Two Pointers
 │
 ├── Contiguous subarray?
 │      └── Sliding Window / Prefix Sum
 │
 ├── Need pairs?
 │      └── Two Pointers / Hash Map
 │
 ├── Need max/min?
 │      └── Heap / Sliding Window / Greedy
 │
 └── Need ordering?
        └── Sorting

For trees:

TREE
 │
 ├── Need explore everything?
 │      ├── DFS
 │      └── BFS
 │
 ├── Need shortest levels?
 │      └── BFS
 │
 ├── Need subtree information?
 │      └── DFS / recursion
 │
 └── Binary Search Tree?
        └── exploit ordering

For graphs:

GRAPH
 │
 ├── Connected?
 │      └── DFS / BFS / Union Find
 │
 ├── Shortest path?
 │      ├── BFS
 │      └── Dijkstra
 │
 ├── Dependencies?
 │      └── Topological Sort
 │
 └── Explore possibilities?
        └── DFS / Backtracking

That pattern recognition is what I want to build.

## 9. Blind 75 sequence I'd use for you

I would not blindly follow the original list order.

I'd use this progression:

Stage 1 — Arrays & Hashing

Start here.

1. Contains Duplicate
2. Valid Anagram
3. Two Sum
4. Group Anagrams
5. Top K Frequent Elements
6. Product of Array Except Self
7. Valid Sudoku
8. Encode and Decode Strings
9. Longest Consecutive Sequence

You'll learn:

list
dict
set
counting
lookup
sorting
prefix/suffix
Stage 2 — Two Pointers
10. Valid Palindrome
11. Two Sum II
12. 3Sum
13. Container With Most Water
14. Trapping Rain Water
Stage 3 — Sliding Window
15. Best Time to Buy and Sell Stock
16. Longest Substring Without Repeating Characters
17. Longest Repeating Character Replacement
18. Permutation in String
19. Minimum Window Substring
20. Sliding Window Maximum
Stage 4 — Stack
21. Valid Parentheses
22. Min Stack
23. Evaluate Reverse Polish Notation
24. Generate Parentheses
25. Daily Temperatures
26. Car Fleet
27. Largest Rectangle in Histogram
Stage 5 — Binary Search
28. Binary Search
29. Search a 2D Matrix
30. Koko Eating Bananas
31. Find Minimum in Rotated Sorted Array
32. Search in Rotated Sorted Array
33. Time Based Key-Value Store
34. Median of Two Sorted Arrays

The last one is intentionally difficult.

We don't need to rush there.

Stage 6 — Linked Lists
35. Reverse Linked List
36. Merge Two Sorted Lists
37. Reorder List
38. Remove Nth Node From End
39. Copy List With Random Pointer
40. Add Two Numbers
41. Linked List Cycle
42. Find the Duplicate Number
43. LRU Cache
Stage 7 — Trees
44. Invert Binary Tree
45. Maximum Depth
46. Diameter of Binary Tree
47. Balanced Binary Tree
48. Same Tree
49. Subtree of Another Tree
50. Lowest Common Ancestor of BST
51. Binary Tree Level Order Traversal
52. Binary Tree Right Side View
53. Count Good Nodes
54. Validate Binary Search Tree
55. Kth Smallest Element in BST
56. Construct Binary Tree
57. Binary Tree Maximum Path Sum
58. Serialize and Deserialize Binary Tree
Stage 8 — Heaps / Priority Queues
59. Kth Largest Element
60. Last Stone Weight
61. K Closest Points
62. Kth Largest Element in a Stream
63. Task Scheduler
64. Find Median from Data Stream
Stage 9 — Backtracking
65. Subsets
66. Combination Sum
67. Permutations
68. Subsets II
69. Combination Sum II
70. Word Search
71. Palindrome Partitioning
72. Letter Combinations
Stage 10 — Graphs / DP / Greedy

We'll finish with:

Graphs
DFS / BFS
Union Find
Topological Sort
Dijkstra

Dynamic Programming
1D DP
2D DP
Knapsack-style problems

Greedy
Intervals
Advanced problems

And importantly, we won't treat the 75th problem as the finish line.

The objective is:

See unfamiliar problem → recognize likely pattern → formulate approach → code it.

## 10. Your "interview notebook"

I'd also keep:

dsa-python/
└── review/
    ├── patterns.md
    ├── data_structures.md
    ├── mistakes.md
    ├── interview_questions.md
    └── weekly_reviews/
patterns.md

Eventually this becomes your personal cheat sheet:

# DSA Patterns

## Hash Map

Use when:
- Need fast lookup
- Counting occurrences
- Finding complements
- Grouping

Typical:
    dict / defaultdict / Counter

---

## Two Pointers

Use when:
- Array/string
- Often sorted
- Looking for pairs
- Comparing ends

Typical:

left = 0
right = len(nums) - 1

while left < right:
    ...

---

## Sliding Window

Use when:
- Contiguous substring/subarray
- Need longest/shortest
- Maintain a changing range

Typical:

left = 0

for right in range(len(nums)):
    ...

This becomes your own DSA reference manual.

## 11. Your mistake journal

This is one of the highest-value parts.

# Mistakes

## Two Sum

### Mistake

I initially used nested loops.

### Why

I focused on finding the pair instead of asking
what information I could remember.

### Lesson

When I repeatedly search for something:

→ consider a Hash Map / Set.

---

## 3Sum

### Mistake

Forgot to skip duplicates.

### Lesson

When using sorting + two pointers,
explicitly consider duplicate values.

Over time this becomes extremely valuable because your interview weaknesses become explicit.

## 12. We will also practice speaking

This is important for technical interviews.

After solving a problem, I'll ask you to explain it like this:

"I'll start with a brute-force approach..."

"The problem with that approach is..."

"I can improve this using..."

"I'll use a hash map because..."

"As I iterate through the array..."

"The time complexity is..."

"The space complexity is..."

You already know Big-O, so we don't need to spend time teaching it.

The skill we're building is communicating your reasoning while coding.

## 13. How AI'll act as your tutor

You can send me things like:

"Give me today's problem."

I'll give you the problem without the solution.

Or:

"I'm stuck."

I'll give you Hint 1.

Then:

"Another hint."

I'll give you Hint 2.

Or:

"Show me the solution."

We'll dissect it.

You can also paste your code:

"Here's my solution. Don't give me the answer.
Tell me what's wrong."

I'll act like an interviewer.

Or:

"Interview me on Two Sum."

I'll conduct an actual mock interview.

## 14. One thing I would change about the Blind 75 approach

Don't aim for:

75 problems completed.

Aim for:

75 problems understood + 30–50 patterns internalized + repeated retrieval practice.

Someone who memorizes 75 LeetCode solutions can still get destroyed by an unfamiliar problem.

Someone who understands:

Hashing
Two Pointers
Sliding Window
Binary Search
Stack
DFS
BFS
Heap
Backtracking
Dynamic Programming
Greedy
Graph traversal

can attack problems they've never seen before.

That's the person we're trying to create.

## 15. Your first week

I'd start you here:

Day 1
Data structure:
    Hash Set

Problems:
    Contains Duplicate
    Valid Anagram
Day 2
Data structure:
    Hash Map

Problems:
    Two Sum
    Group Anagrams
Day 3
Hash Map + Heap

Problem:
    Top K Frequent Elements
Day 4
Prefix/Suffix

Problem:
    Product of Array Except Self
Day 5
Hash Set

Problems:
    Valid Sudoku
    Longest Consecutive Sequence
Day 6

Review only

Redo 3–5 problems without looking at your previous code.

Day 7

Interview simulation

I'll give you 2–3 problems without telling you the pattern.

You have to determine:

What data structure?
What pattern?
Brute force?
Optimization?
Implementation?
Complexity?
Explanation?

That's where the learning starts becoming real.
