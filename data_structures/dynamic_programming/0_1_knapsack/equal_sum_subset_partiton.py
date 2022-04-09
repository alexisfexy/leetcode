from typing import List


class EqualSumSubset(object):
    """
    Given a set of positive numbers:
    - find if we can partition it into two subsets
    - such that the sum of elements in both the subsets is equal.
    """
    def brute_force_recursive_soln(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        sub_group_sum = total_sum / 2

        def _helper(nums: List[int], sum_remaining: int = sub_group_sum, current_index: int = 0):
            if current_index >= len(nums) - 1 or sum_remaining <= 0:
                return False
            if sum_remaining == 0:
                return True
            current_value = nums[current_index]
            include_sum = False
            if sum_remaining == current_value:
                return True
            elif current_value <= sum_remaining:
                include_sum = _helper(nums, sum_remaining - nums[current_index], current_index + 1)
            exclude_sum = _helper(nums, sum_remaining, current_index + 1)
            return include_sum or exclude_sum
        return _helper(nums)

    def dp_recursive_soln(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        sub_group_sum = int(total_sum / 2)

        previous_calcs: List[List[int]] = [[-1 for _ in range(sub_group_sum + 1)] for _ in range(len(nums))]

        def _helper(nums: List[int], sum_remaining: int, current_index: int, previous_calcs: List[List[int]]):
            if current_index >= len(nums) - 1 or sum_remaining <= 0:
                return False
            if sum_remaining == 0:
                return True
            if previous_calcs[current_index][sum_remaining] >= 0:
                return previous_calcs[current_index][sum_remaining]
            current_value = nums[current_index]
            include_sum = False
            if sum_remaining == current_value:
                return True
            elif current_value <= sum_remaining:
                include_sum = _helper(nums, sum_remaining - nums[current_index], current_index + 1, previous_calcs)
            exclude_sum = _helper(nums, sum_remaining, current_index + 1, previous_calcs)
            previous_calcs[current_index][sum_remaining] = include_sum or exclude_sum
            return include_sum or exclude_sum
        return _helper(nums, sub_group_sum, 0, previous_calcs=previous_calcs)

    def dp_tabulation_soln(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        sub_group_sum = int(total_sum / 2)
        tracker_table: List[List[bool]] = [[False for _ in range(sub_group_sum + 1)] for _ in range(len(nums))]

        for index, value in enumerate(nums):
            for capacity in range(sub_group_sum + 1):
                if capacity == 0 or capacity == value or tracker_table[index-1][capacity]:
                    tracker_table[index][capacity] = True
                elif capacity >= value:
                    remaining_sum = capacity - value
                    tracker_table[index][capacity] = tracker_table[index-1][remaining_sum]
        return tracker_table[len(nums)-1][sub_group_sum]


if __name__ == "__main__":
    x = EqualSumSubset().dp_tabulation_soln([1,5,11,5])
    print(x)