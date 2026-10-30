def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return the indices of two distinct elements that sum to target.

    Args:
        nums: A list of integers.
        target: The required sum.

    Returns:
        The indices of the two elements that sum to target.
    """
    # TODO: Implement a dictionary
    seen = {}
    # TODO Iterate through nums
    for index, num in  enumerate(nums):
    # TODO Calculate the complement
        complement = target - num
    # TODO Check to see if complement is in dictionary
        if complement in seen:
            return [seen[complement], index]
        else:
            seen[num] = index

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