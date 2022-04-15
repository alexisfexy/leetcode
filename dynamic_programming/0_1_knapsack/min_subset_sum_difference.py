from typing import List


class MinimumSubsetSumDifference(object):
    """
    Given a set of positive numbers:
     - partition the set into two subsets with a minimum difference between their subset sums.
    """

    def brute_force_soln(self, nums: List[int]) -> int:
        mins = set()
        for index, num in enumerate(nums):
            include_sum = num
            second_sum = sum(nums[:index] + nums[index + 1:])
            min_diff = abs(include_sum - second_sum)
            for second_index in range(index + 1, len(nums)):
                val = nums[second_index]
                potential_sum = include_sum + val
                potential_second = second_sum - val
                potential_diff = abs(potential_second - potential_sum)
                if potential_diff < min_diff:
                    min_diff = potential_diff
                    include_sum = potential_sum
                    second_sum = potential_second
                elif potential_diff > min_diff:
                    two_sum = num + val
                    exclude_sum = sum(nums[:index] + nums[index + 1:]) - val
                    check_diff = abs(two_sum - exclude_sum)
                    if potential_diff < check_diff:
                        include_sum = two_sum
                        second_sum = exclude_sum
                        min_diff = check_diff
            mins.add(min_diff)
        return min(mins)

    def brute_force_recursive_soln(self, nums: List[int]) -> int:

        def recursive_helper(include_sum: int, exclude_sum: int, nums: List[int], current_index: int):
            if current_index >= len(nums):
                return abs(include_sum - exclude_sum)
            include_min = recursive_helper(include_sum + nums[current_index], exclude_sum, nums, current_index + 1)
            exclude_min = recursive_helper(include_sum, exclude_sum + nums[current_index], nums, current_index + 1)
            return min(include_min, exclude_min)

        return recursive_helper(0, 0, nums, 0)

    def dp_memoization_soln(self, nums: List[int]) -> int:
        def _recursive_helper(include_sum: int, exclude_sum: int, nums: List[int], current_index: int):
            if current_index >= len(nums):
                return abs(include_sum - exclude_sum)
            if previously_calc[current_index][include_sum] >= 0:
                return previously_calc[current_index][include_sum]
            include_min = _recursive_helper(include_sum + nums[current_index], exclude_sum, nums, current_index + 1)
            exclude_min = _recursive_helper(include_sum, exclude_sum + nums[current_index], nums, current_index + 1)
            previously_calc[current_index][include_sum] = min(include_min, exclude_min)
            return previously_calc[current_index][include_sum]

        previously_calc = [[-1 for _ in range(sum(nums) + 1)] for _ in range(len(nums))]
        return _recursive_helper(0, 0, nums, 0)

    def dp_tabulation_soln(self, nums: List[int]) -> int:
        equal_half_sum = int(sum(nums) / 2)
        num_length = len(nums)
        table_tracker = [[False for _ in range(equal_half_sum + 1)] for _ in range(num_length)]

        # Populate table
        for index, value in enumerate(nums):
            for sum_value in range(equal_half_sum + 1):
                if sum_value == 0 or sum_value == value or table_tracker[index - 1][sum_value]:
                    table_tracker[index][sum_value] = True
                elif value < sum_value:  # achievable with this number if remainder is also achievable
                    table_tracker[index][sum_value] = table_tracker[index - 1][sum_value - value]

        # Find first true sum in final row (using all numbers)
        sum_one = 0
        for sum_value in range(equal_half_sum, -1, -1):
            if table_tracker[num_length - 1][sum_value]:
                sum_one = sum_value
                break
        return abs(sum_one - (sum(nums) - sum_one))

if __name__ == "__main__":
    sample_input = [1, 2, 3, 9]
    sample_92_input = [1, 3, 4, 100]
    x = MinimumSubsetSumDifference().dp_tabulation_soln(sample_92_input)
    print(x)
