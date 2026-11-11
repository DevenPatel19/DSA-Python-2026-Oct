"""
============================================================
Blind 75 — Product of Array Except Self
Pattern: Arrays & Hashing
Difficulty: Medium
============================================================

PROBLEM
-------
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[i].

The solution must NOT use division.

Try to solve the problem in:
    Time Complexity: O(n)
    Auxiliary Space Complexity: O(1)
    (The output array does not count toward auxiliary space.)


EXAMPLES
--------
Example 1:
    Input:  nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

    Explanation:
        answer[0] = 2 * 3 * 4 = 24
        answer[1] = 1 * 3 * 4 = 12
        answer[2] = 1 * 2 * 4 = 8
        answer[3] = 1 * 2 * 3 = 6

Example 2:
    Input:  nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]

    Explanation:
        Each position contains the product of all other
        elements. The zero affects every result except
        the result corresponding to its own index.

Example 3:
    Input:  nums = [2, 3]
    Output: [3, 2]

Example 4:
    Input:  nums = [0, 5]
    Output: [5, 0]


CONSTRAINTS
-----------
- 2 <= len(nums) <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is
  guaranteed to fit in a 32-bit integer.
- Division is not allowed.


INTERVIEW GOAL
--------------
Develop an algorithm that calculates the product of all
elements except the element at the current index.

Consider how to calculate each answer without repeatedly
traversing the entire array.

Try to achieve:
    Time Complexity: O(n)
    Auxiliary Space Complexity: O(1)

Where n represents the number of elements in nums.

The output array is excluded from auxiliary space.


HINTS
-----
DO NOT look at these until you have attempted the problem.

Hint 1:
    For each index, which elements should contribute
    to its answer?

Hint 2:
    Can you separate the elements before an index from
    the elements after that index?

Hint 3:
    What if you calculated the product of all elements
    to the left of each index first?

Hint 4:
    How could you calculate the product of all elements
    to the right of each index?

Hint 5:
    Can you combine the left and right products without
    creating two additional arrays?

Hint 6:
    What should the initial product be when no elements
    have been processed? Think about the multiplicative
    identity.


YOUR APPROACH
-------------
Before writing code, answer these questions:

1. Why can't we simply multiply all elements and divide
   by nums[i]?

2. What should answer[i] represent?

3. What is the prefix product of an element?

4. What is the suffix product of an element?

5. How can we calculate the product of all elements
   before the current index?

6. How can we calculate the product of all elements
   after the current index?

7. Why is 1 used as the initial product value?

8. How can we combine prefix and suffix products
   to calculate answer[i]?

9. How can we perform this calculation using only
   the output array and a single additional variable?


FUNCTION REQUIREMENTS
---------------------
productExceptSelf(nums: list[int]) -> list[int]

    Accepts a list of integers.

    Returns a list where each position contains the
    product of all elements except the element at
    the corresponding index.

    Requirements:
        - Do not use division.
        - Aim for O(n) time complexity.
        - Aim for O(1) auxiliary space complexity,
          excluding the output array.


TEST CASES
----------
Run the function against these cases:

1. [1, 2, 3, 4]
   -> [24, 12, 8, 6]

2. [-1, 1, 0, -3, 3]
   -> [0, 0, 9, 0, 0]

3. [2, 3]
   -> [3, 2]

4. [0, 5]
   -> [5, 0]

5. [5, 0]
   -> [0, 5]

6. [1, 1, 1, 1]
   -> [1, 1, 1, 1]

7. [-1, -2, -3, -4]
   -> [-24, -12, -8, -6]

8. [0, 0, 3, 4]
   -> [0, 0, 0, 0]

9. [2, 0, 3, 4]
   -> [0, 24, 0, 0]

10. [1, 2, 0, 4, 5]
    -> [0, 0, 40, 0, 0]

11. [-2, 3, 4]
    -> [12, -8, -6]

12. [2, -3]
    -> [-3, 2]
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Calculate the product of all elements except
    the element at the current index.

    Args:
        nums: A list of integers.

    Returns:
        A list containing the product of all other
        elements for each corresponding index.
    """

    # TODO: Initialize output array.
    # TODO: Initialize prefix product variable.

    # TODO: First traversal - calculate prefix products.
        # TODO: Store the current prefix product.
        # TODO: Update the prefix product.

    # TODO: Initialize suffix product variable.

    # TODO: Second traversal - calculate suffix products.
        # TODO: Multiply the current output value
        #       by the suffix product.
        # TODO: Update the suffix product.

    # TODO: Return output array.

    pass


if __name__ == "__main__":

    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([0, 5], [5, 0]),
        ([5, 0], [0, 5]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-1, -2, -3, -4], [-24, -12, -8, -6]),
        ([0, 0, 3, 4], [0, 0, 0, 0]),
        ([2, 0, 3, 4], [0, 24, 0, 0]),
        ([1, 2, 0, 4, 5], [0, 0, 40, 0, 0]),
        ([-2, 3, 4], [12, -8, -6]),
        ([2, -3], [-3, 2]),
    ]

    passed_count = 0
    total_count = len(test_cases)

    print("=" * 50)
    print("PRODUCT OF ARRAY EXCEPT SELF - TEST RESULTS")
    print("=" * 50)

    for nums, expected in test_cases:

        result = productExceptSelf(nums)

        passed = result == expected

        if passed:
            passed_count += 1

        status = "PASS" if passed else "FAIL"

        print(f"Input:    {nums}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Status:   {status}")
        print("-" * 50)

    print(f"\nTests passed: {passed_count}/{total_count}")

    if passed_count == total_count:
        print("ALL TESTS PASSED!")
    else:
        print(
            f"TESTS FAILED: "
            f"{total_count - passed_count} test(s) failed."
        )
