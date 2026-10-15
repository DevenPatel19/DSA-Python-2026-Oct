def contains_duplicate(nums: list[int]) -> bool:
    """
    Determine whether nums contains any duplicate values.

    Args:
        nums: A list of integers.

    Returns:
        True if a duplicate exists, otherwise False.
    """

    # TODO: Implement your solution here.
    seen = set()
    for num in nums:
        if num in seen:
            return True
        
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