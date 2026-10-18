"""
============================================================
Blind 75 — #5: Top K Frequent Elements
Pattern: Arrays & Hashing
Difficulty: Medium
============================================================


PROBLEM
-------
Given an integer array `nums` and an integer `k`, return the `k`
most frequent elements. You may return the answer in any order.


EXAMPLES
--------
Example 1:
    Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]


Example 2:
    Input:  nums = [1], k = 1
    Output: [1]


Example 3:
    Input:  nums = [4, 4, 4, 6, 6, 7, 7, 7], k = 2
    Output: [7, 4]  (or [4, 7])


CONSTRAINTS
-----------
- 1 <= len(nums) <= 100,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000
- 1 <= k <= number of distinct values in nums


INTERVIEW GOAL
--------------
Try to solve this in O(n) time using frequency counting
and bucket sort.


HINTS
------
Do NOT look at these until you have attempted the problem.


Hint 1:
    First, count how many times each distinct number appears.


Hint 2:
    A number cannot appear more times than the length of nums.


Hint 3:
    Create buckets indexed by frequency. Bucket i should hold
    every number that appears exactly i times.


Hint 4:
    Scan buckets from the highest frequency down to the lowest,
    collecting numbers until you have k results.


YOUR APPROACH
-------------
Before writing code, answer these questions:


1. What information do I need to track for each distinct number?


2. Which data structure should I use for the frequency counts?


3. How can I organize numbers by their frequency without sorting
   every distinct number?


4. What is the largest possible frequency in an array of length n,
   and how does that determine the number of buckets?


5. In which direction should I scan the buckets, and when do I stop?


TEST CASES
----------
Run the function against these cases:


1. [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
2. [1], k = 1 -> [1]
3. [4, 4, 4, 6, 6, 7, 7, 7], k = 2 -> [7, 4] or [4, 7]
4. [1, 2], k = 2 -> [1, 2] or [2, 1]
5. [3, 3, 3, 3], k = 1 -> [3]
6. [1, 1, 2, 2, 3, 3], k = 3 -> [1, 2, 3] in any order
"""



def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Return the k most frequent elements in nums.


    Args:
        nums: A list of integers.
        k: The number of most frequent elements to return.


    Returns:
        A list containing the k most frequent integers.
        The order of the returned list does not matter.
    """


    # TODO: Implement your solution here.

    # TODO 1: Create a dictionary to count how often each number appears.
    counts = {}

    # TODO 2: Iterate through nums and update each number's frequency.
    for num in nums:
        if num in counts:
            counts[num] +=1
        else:
            counts[num] = 1


    # TODO 3: Create n + 1 buckets. Bucket i will hold all numbers
    #         that appear exactly i times.
    buckets = [[] for _ in range(len(nums)+1)]

    # TODO 4: Place each distinct number into the bucket matching
    #         its frequency.
    for num, freq in counts.items():
        buckets[freq].append(num)

    # TODO 5: Scan buckets from the highest frequency down to frequency 1.
    result = []
    
    for freq in range(len(nums),0, -1):
        for num in buckets[freq]:
    #         Add numbers to the result until it contains k numbers.
            result.append(num)
            if len(result) == k:
                break
        if len(result) == k:
            break

    # TODO 6: Return the result.
    return result

if __name__ == "__main__":
    # Basic test cases
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 4, 4, 6, 6, 7, 7, 7], 2, {7, 4}),
        ([1, 2], 2, {1, 2}),
        ([3, 3, 3, 3], 1, {3}),
        ([1, 1, 2, 2, 3, 3], 3, {1, 2, 3}),
    ]


    all_passed = True


    for nums, k, expected in test_cases:
        result = top_k_frequent(nums, k)
        passed = set(result) == expected and len(result) == k


        all_passed = all_passed and passed


        print(f"Input:    nums = {nums}, k = {k}")
        print(f"Expected: any order containing {sorted(expected)}")
        print(f"Result:   {result}")
        print(f"Passed:   {passed}")
        print("-" * 40)


    print(f"All tests passed: {all_passed}")