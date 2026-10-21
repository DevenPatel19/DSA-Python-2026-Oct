"""
============================================================
Blind 75 — #1: Contains Duplicate
Pattern: Arrays & Hashing
Difficulty: Easy
============================================================

PROBLEM
-------
Given an integer array `nums`, return True if any value appears
at least twice in the array, and return False if every element
is distinct.


EXAMPLES
--------
Example 1:
    Input:  nums = [1, 2, 3, 1]
    Output: True

Example 2:
    Input:  nums = [1, 2, 3, 4]
    Output: False

Example 3:
    Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    Output: True


CONSTRAINTS
-----------
- 1 <= len(nums) <= 100,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000


INTERVIEW GOAL
--------------
Try to solve this in O(n) time.


HINTS
------
Do NOT look at these until you have attempted the problem.

Hint 1:
    What information could you keep track of as you
    iterate through the array?

Hint 2:
    You need to quickly determine whether you've seen
    a value before.

Hint 3:
    Which Python data structure provides very fast
    membership checking?


YOUR APPROACH
-------------
Before writing code, answer these questions:

1. What information do I need to remember?

2. What data structure should I use?

3. What should happen when I encounter a number I've
   already seen?

4. What should happen when I encounter a new number?


TEST CASES
----------
Run the function against these cases:

1. [1, 2, 3, 1] -> True
2. [1, 2, 3, 4] -> False
3. [1, 1] -> True
4. [1] -> False
5. [1, 2, 3, 4, 5, 5] -> True
"""


def contains_duplicate(nums: list[int]) -> bool:
    """
    Determine whether nums contains any duplicate values.

    Args:
        nums: A list of integers.

    Returns:
        True if a duplicate exists, otherwise False.
    """

    # TODO: Implement your solution here.
    # TODO  Select and Instantiate a structure to hold values (have I seen this before usually means hashset/set)
    seen = set()
        
        # TODO Go through the input list and if nothing is duplicated return False
    for num in nums:
        # TODO if the value isn't in the holding structure add it
        if num in seen:
            return True
                #TODO if the value is in the holding structure return True
        else:
            seen.add(num)
    return False
             
         

if __name__ == "__main__":
    # Basic test cases
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1], True),
        ([1], False),
        ([1, 2, 3, 4, 5, 5], True),
    ]

    for nums, expected in test_cases:
        result = contains_duplicate(nums)

        print(f"Input:    {nums}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print(f"Passed:   {result == expected}")
        print("-" * 40)