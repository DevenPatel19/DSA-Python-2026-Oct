"""
============================================================
Blind 75 — #3: Two Sum
Pattern: Arrays & Hashing
Difficulty: Easy
============================================================

PROBLEM
-------
Given an array of integers nums and an integer target,
return the indices of the two numbers that add up to target.

You may assume that each input has exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


EXAMPLES
--------
Example 1:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Example 2:
    Input:  nums = [3, 2, 4], target = 6
    Output: [1, 2]

Example 3:
    Input:  nums = [3, 3], target = 6
    Output: [0, 1]


CONSTRAINTS
-----------
- 2 <= len(nums) <= 10,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000
- -1,000,000,000 <= target <= 1,000,000,000
- Exactly one valid answer exists.


INTERVIEW GOAL
--------------
Solve this problem in O(n) time using a hash map.


HINTS
-----
Do NOT look at these until you have attempted the problem.

Hint 1:
    What information could you store as you iterate
    through the array?

Hint 2:
    If you know the current number and the target,
    can you calculate the number you need?

Hint 3:
    What Python data structure provides fast lookups?

Hint 4:
    Should you check whether the complement exists
    before or after adding the current number?


YOUR APPROACH
-------------
Before writing code, answer these questions:

1. What information do I need to remember?

2. Which data structure should I use?

3. How do I calculate the complement?

4. What should I check before adding the current
   number to my dictionary?

5. What should I store as the dictionary value?

6. What should happen when I find the complement?


TEST CASES
----------
Run the function against these cases:

1. [2, 7, 11, 15], target = 9 -> [0, 1]
2. [3, 2, 4], target = 6 -> [1, 2]
3. [3, 3], target = 6 -> [0, 1]
4. [-1, -2, -3, -4, -5], target = -8 -> [2, 4]
5. [0, 4, 3, 0], target = 0 -> [0, 3]


============================================================
IMPLEMENTATION
============================================================
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return the indices of two distinct elements that sum to target.

    Args:
        nums: A list of integers.
        target: The required sum.

    Returns:
        The indices of the two elements that sum to target.
    """

    # TODO 1: Create a dictionary to store numbers and their indices.

    # TODO 2: Iterate through nums using enumerate().

    # TODO 3: Calculate the complement.

    # TODO 4: Check whether the complement exists in the dictionary.

    # TODO 5: If found, return the two indices.

    # TODO 6: If not found, store the current number and its index.

    pass


def run_tests() -> None:
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]

    passed_count = 0
    total_count = len(test_cases)

    print("=" * 45)
    print("TWO SUM - TEST RESULTS")
    print("=" * 45)

    for nums, target, expected in test_cases:
        result = two_sum(nums, target)

        # Verify both indices match, regardless of order.
        passed = (
            result is not None
            and sorted(result) == sorted(expected)
            and len(result) == 2
            and result[0] != result[1]
            and nums[result[0]] + nums[result[1]] == target
        )

        if passed:
            passed_count += 1

        status = "PASS" if passed else "FAIL"

        print(f"Input:    nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")
        print(f"Status:   {status}")
        print("-" * 45)

    print(f"\nTests passed: {passed_count}/{total_count}")

    if passed_count == total_count:
        print("ALL TESTS PASSED!")
    else:
        print(
            f"TESTS FAILED: "
            f"{total_count - passed_count} test(s) failed."
        )


if __name__ == "__main__":
    run_tests()