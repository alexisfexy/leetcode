from typing import List


class SubsetSum(object):

    """
    Given a set of positive numbers:
    - determine if there exists a subset whose sum is equal to a given number ‘S’.
    """

    def brute_force_solution(self, nums: List[int], desired_sum: int) -> bool:
        def _helper(nums: List[int], remaining_sum: int, index: int):
            if remaining_sum == 0:
                return True
            elif index >= len(nums) or index < 0:
                return False
            current_value = nums[index]
            include_sum = False
            if current_value == remaining_sum:
                return True
            elif current_value < remaining_sum:
                include_sum = _helper(nums, remaining_sum-current_value, index+1)
            exclude_sum = _helper(nums, remaining_sum, index+1)
            return include_sum or exclude_sum
        return _helper(nums, remaining_sum=desired_sum, index=0)

    def dp_memo_soln(self, nums: List[int], desired_sum: int) -> bool:
        previously_calc = [[-1 for _ in range(0, desired_sum+1)] for _ in range(len(nums))]

        def _helper(nums: List[int], remaining_sum: int, index: int, previously_calc: List[List[int]]):
            if remaining_sum == 0:
                return True
            elif index >= len(nums) or index < 0:
                return False
            if previously_calc[index][remaining_sum] > 0:
                return previously_calc[index][remaining_sum]
            current_value = nums[index]
            include_sum = False
            if current_value == remaining_sum:
                return True
            elif current_value < remaining_sum:
                include_sum = _helper(nums, remaining_sum - current_value, index + 1, previously_calc)
            exclude_sum = _helper(nums, remaining_sum, index + 1, previously_calc)
            previously_calc[index][remaining_sum] = include_sum or exclude_sum
            return include_sum or exclude_sum

        return _helper(nums, remaining_sum=desired_sum, index=0, previously_calc=previously_calc)

    def dp_tabulation_soln(self, nums: List[int], desired_sum: int) -> bool:
        # Columns: capacity/remaining sum
        # Rows: index of items up to this point
        table = [[False for _ in range(0, desired_sum + 1)] for _ in range(len(nums))]
        for index, value in enumerate(nums):
            for capacity in range(desired_sum + 1):
                if capacity == 0 or capacity == value or table[index-1][capacity]:
                    table[index][capacity] = True
                elif capacity > value:  # Use it, but is the remainder achievable
                    remaining_sum = capacity-value
                    table[index][capacity] = table[index-1][remaining_sum]
        print(table)
        return table[len(nums)-1][desired_sum]


if __name__ == "__main__":
    sample_false_input = [[1, 3, 4, 8], 6]
    sample_true_input = [[1, 2, 7, 1, 5], 10]
    x = SubsetSum().dp_tabulation_soln(*sample_true_input)
    print(x)