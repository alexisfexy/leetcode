from typing import List


class CountSubsetSum(object):
    """
    Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

    Example:
        Input: {1, 1, 2, 3}, S=4
        Output: 3
        Explanation: The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
        Note that we have two similar sets {1, 3}, because we have two '1' in our input.
    """

    def brute_force_soln(self, nums: List[int], target: int):

        def _recursive_helper(nums: List[int], target: int, current_index: int):
            if current_index >= len(nums) or target < 0:
                return 0
            val = nums[current_index]
            if val == target:
                return 1
            include_sum = 0
            if val < target:
                include_sum = _recursive_helper(nums, target - val, current_index + 1)
            exclude_sum = _recursive_helper(nums, target, current_index + 1)
            return include_sum + exclude_sum

        return _recursive_helper(nums, target, 0)

    def dp_memoization_soln(self, nums: List[int], target: int):
        previously_calc = [[-1 for _ in range(target+1)] for _ in range(len(nums))]

        def _recursive_helper(nums: List[int], target: int, current_index: int):
            if current_index >= len(nums) or target < 0:
                return 0
            if previously_calc[current_index][target] >= 0:
                return previously_calc[current_index][target]
            val = nums[current_index]
            if val == target:
                return 1
            include_sum = 0
            if val < target:
                include_sum = _recursive_helper(nums, target - val, current_index + 1)
            exclude_sum = _recursive_helper(nums, target, current_index + 1)
            previously_calc[current_index][target] = include_sum + exclude_sum
            return previously_calc[current_index][target]

        return _recursive_helper(nums, target, 0)


if __name__ == "__main__":
    args = ([1, 1, 2, 3], 4)
    sample_args = ([1, 2, 7, 1, 5], 9)
    x = CountSubsetSum().dp_memoization_soln(*sample_args)
    print(x)
