
"""
============================================================
Blind 75 — Longest Consecutive Sequence
Pattern: Arrays & Hashing
Difficulty: Medium
============================================================

PROBLEM
-------
Given an unsorted array of integers nums, return the length
of the longest consecutive elements sequence.

A consecutive sequence consists of numbers that follow one
another without gaps.

The numbers do NOT need to appear next to each other in the
original array.

#! Your algorithm must run in:

    Time Complexity: O(n)
    Auxiliary Space Complexity: O(n)

------------------------------------------------------------
EXAMPLES
------------------------------------------------------------

Example 1:
    Input:  nums = [100, 4, 200, 1, 3, 2]
    Output: 4

    Explanation:
    The longest consecutive sequence is [1, 2, 3, 4].
    Its length is 4.

Example 2:
    Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9

    Explanation:
    The longest consecutive sequence is
    [0, 1, 2, 3, 4, 5, 6, 7, 8].
    Its length is 9.

Example 3:
    Input:  nums = [1, 0, 1, 2]
    Output: 3

    Explanation:
    The longest consecutive sequence is [0, 1, 2].
    Duplicate values do not increase the sequence length.

------------------------------------------------------------
CONSTRAINTS
------------------------------------------------------------

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

------------------------------------------------------------
FUNCTION TEMPLATE
------------------------------------------------------------
"""

def longestConsecutive(nums: list[int]) -> int:

    # --------------------------------------------------------
    # STEP 1: Initialize variables
    # --------------------------------------------------------

    # Your code here


    # --------------------------------------------------------
    # STEP 2: Build your data structure
    # --------------------------------------------------------

    # Your code here


    # --------------------------------------------------------
    # STEP 3: Find the beginning of each sequence
    # --------------------------------------------------------

    # Your code here


    # --------------------------------------------------------
    # STEP 4: Count consecutive numbers
    # --------------------------------------------------------

    # Your code here


    # --------------------------------------------------------
    # STEP 5: Return the longest sequence length
    # --------------------------------------------------------

    # Your code here
    pass

# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------
if __name__ == "__main__":
    
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([], 0),
        ([5], 1),
        ([1, 2, 3, 4, 5], 5),
        ([9, 1, 4, 7, 3, 2, 6, 8, 0, 5], 10),
        ([-2, -1, 0, 1], 4),
    ]   


# ------------------------------------------------------------
# RUN TESTS
# ------------------------------------------------------------

passed_count = 0
total_count = len(test_cases)

print("=" * 50)
print("LONGEST CONSECUTIVE SEQUENCE - TEST RESULTS")
print("=" * 50)

for nums, expected in test_cases:
    result = longestConsecutive(nums)
    
    passed = result == expected
    
    if passed:
        passed_count += 1
        
    status = "PASS" if passed else "FAIL"

    print(f"Input:    {nums}")
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    print(f"Passed:   {result == expected}")
    print("-" * 50)

print(f"\nTests passed: {passed_count}/{total_count}")

if passed_count ==  total_count:
    print("ALL TESTS PASSED!")
else:
    print(
        f"TESTS FAILED: "
        f"{total_count - passed_count} test(s) failed."
    )