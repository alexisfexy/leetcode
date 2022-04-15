import math
from typing import List


class MinCoinChange(object):

    """
    Given an infinite supply of ‘n’ coin denominations
    and a total money amount, we are asked to find the minimum
    number of coins needed to make up that amount.
    """

    def brute_force_soln(self, denoms: List[int], total_money: int):

        def _recursive_helper(denoms: List[int], remaining_money: int, current_index: int):
            if remaining_money == 0:
                return 0
            elif current_index >= len(denoms):
                return math.inf
            denom_value = denoms[current_index]
            exclude_sum = _recursive_helper(denoms, remaining_money, current_index+1)
            include_sum = math.inf
            if denom_value <= remaining_money:
                result = _recursive_helper(denoms, remaining_money-denom_value, current_index)
                if result != math.inf:
                    include_sum = result + 1
            return min(include_sum, exclude_sum)
        return _recursive_helper(denoms, total_money, 0)

    def dp_memoization_soln(self, denoms: List[int], total_money: int):
        previous_calcs = [[-1 for _ in range(total_money+1)] for _ in range(len(denoms))]
        def _recursive_helper(denoms: List[int], remaining_money: int, current_index: int):
            if current_index >= len(denoms):
                return math.inf
            elif previous_calcs[current_index][remaining_money] >= 0:
                return previous_calcs[current_index][remaining_money]
            if remaining_money == 0:
                return 0

            denom_value = denoms[current_index]
            exclude_sum = _recursive_helper(denoms, remaining_money, current_index+1)
            include_sum = math.inf
            if denom_value <= remaining_money:
                result = _recursive_helper(denoms, remaining_money-denom_value, current_index)
                if result != math.inf:
                    include_sum = result + 1
            previous_calcs[current_index][remaining_money] = min(include_sum, exclude_sum)
            return previous_calcs[current_index][remaining_money]
        return _recursive_helper(denoms, total_money, 0)

    def dp_tabulation_soln(self, denoms: List[int], total_money: int):
        tracker_table = [[math.inf for _ in range(total_money + 1)] for _ in range(len(denoms))]
        for index, value in enumerate(denoms):
            for goal_amount in range(0, total_money+1):
                if goal_amount == 0:  # Can always achieve this with 0
                    tracker_table[index][goal_amount] = 0
                else:
                    excluding, including = math.inf, math.inf
                    if value <= goal_amount:
                        including = 1 + tracker_table[index][goal_amount-value]
                    if index > 0:
                        excluding = tracker_table[index-1][goal_amount]
                    tracker_table[index][goal_amount] = min(excluding, including)
        return tracker_table[len(denoms)-1][total_money]


if __name__ == "__main__":
    x = MinCoinChange().dp_tabulation_soln([1, 2, 3], 5)
    print(x)