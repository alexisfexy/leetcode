from copy import copy
from typing import List, Dict


class ContainsDuplicates(object):

    def solution(self, nums: List[int]) -> bool:
        set_seen = set()
        for x in nums:
            if x in set_seen:
                return True
            else:
                set_seen.add(x)
        return False

    def faster_solution(self, nums: List[int]) -> bool:
        num_set = set(nums)
        return len(num_set) != len(nums)


class MaximumSubArray(object):
    """
    Given an integer array nums, find the contiguous sub array (containing at least one number)
     which has the largest sum and return its sum.
    """
    def brute_force_soln(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for start_index, number in enumerate(nums):
            max_subarray_sum = number
            running_sum = number
            for index in range(start_index + 1, len(nums)):
                running_sum += nums[index]
                if running_sum > max_subarray_sum:
                    max_subarray_sum = running_sum
            if max_subarray_sum > max_sum:
                max_sum = max_subarray_sum
        return max_sum

    def another_brute_force_soln(self, nums: List[int]) -> int:
        running_totals = [*nums]  # copy(nums)
        max_sub_arrays = nums
        for index, number in enumerate(nums):
            for i in range(0, index):
                running_totals[i] += number
                if running_totals[i] > max_sub_arrays[i]:
                    max_sub_arrays[i] = running_totals[i]
        return max(max_sub_arrays)

    # def recursive_soln(self, nums: List[int]) -> int:



if __name__ == "__main__":
    x = MaximumSubArray().another_brute_force_soln([5,6,7,-10,20])
    print("SOLUTION:")
    print(x)