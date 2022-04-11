from typing import List


class TwoSum(object):
    """
    Given an array of integers nums and an integer target:
    - return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """

    def brute_force_soln(self, nums: List[int], target: int):
        for index, value in enumerate(nums):
            for second_index in range(index + 1, len(nums)):
                if value + nums[second_index] == target:
                    return [index, second_index]

        return []

    def dictionary_soln_number_key(self, nums: List[int], target: int):
        # Key: number, value: index
        # Lookup by remainder
        remainder_index = dict()
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder_index.get(remainder, None) is not None:
                return [remainder_index.get(remainder), index]
            else:
                remainder_index[value] = index
        return []

    def dictionary_soln_remainder_key(self, nums: List[int], target: int):
        # Store remainder, look up by number
        remainder_index = dict()
        for index, value in enumerate(nums):
            if value in remainder_index:
                return [index, remainder_index[value]]
            else: # Store remainder
                remainder = target - value
                remainder_index[remainder] = index
        return []