def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return the indices of two distinct elements that sum to target.

    Args:
        nums: A list of integers.
        target: The required sum.

    Returns:
        The indices of the two elements that sum to target.
    """
    # TODO: Implement the hash map approach.
    # TODO: Implement a dictionary
    seen = {}
    # TODO Iterate through nums
    for index, num in enumerate(nums):
    # TODO Calculate the complement
        complement = target - num
    # TODO Check to see if complement is in dictionary
    # pass
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

    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        assert sorted(result) == sorted(expected), (
            f"two_sum({nums}, {target}): "
            f"expected {expected}, got {result}"
        )

    print(f"All {len(test_cases)} tests passed!")


if __name__ == "__main__":
    run_tests()