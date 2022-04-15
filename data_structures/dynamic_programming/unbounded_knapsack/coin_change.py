from typing import List


class CoinChange(object):
    """
    Given an infinite supply of ‘n’ coin denominations and a total money amount,
    we are asked to find the total number of distinct ways to make up that amount.

    Example:
        Denominations: {1,2,3}
        Total amount: 5
        Output: 5
        Explanation: There are five ways to make the change for '5', here are those ways:
          1. {1,1,1,1,1}
          2. {1,1,1,2}
          3. {1,2,2}
          4. {1,1,3}
          5. {2,3}
    """

    def brute_force_soln(self, denoms: List[int], capacity: int) -> int:

        def _recursive_helper(denoms: List[int], remaining_cap: int, current_index: int):
            if remaining_cap < 0 or current_index >= len(denoms):
                return 0
            curr_denom = denoms[current_index]
            include = 0
            if curr_denom == remaining_cap:
                return 1
            elif curr_denom < remaining_cap:
                include = _recursive_helper(denoms, remaining_cap - curr_denom, current_index)
            exclude = _recursive_helper(denoms, remaining_cap, current_index + 1)
            return include + exclude

        return _recursive_helper(denoms, capacity, 0)

    def dp_memoization_soln(self, denoms: List[int], capacity: int) -> int:
        previously_calc = [[-1 for _ in range(capacity + 1)] for _ in range(len(denoms))]

        def _recursive_helper(denoms: List[int], remaining_cap: int, current_index: int):
            if remaining_cap < 0 or current_index >= len(denoms):
                return 0
            if previously_calc[current_index][remaining_cap] >= 0:
                return previously_calc[current_index][remaining_cap]
            curr_denom = denoms[current_index]
            include = 0
            if curr_denom == remaining_cap:
                return 1
            elif curr_denom < remaining_cap:
                include = _recursive_helper(denoms, remaining_cap - curr_denom, current_index)
            exclude = _recursive_helper(denoms, remaining_cap, current_index + 1)
            previously_calc[current_index][remaining_cap] = include + exclude
            return previously_calc[current_index][remaining_cap]

        return _recursive_helper(denoms, capacity, 0)

    def dp_tabulation_soln(self, denoms: List[int], capacity: int) -> int:
        tracker_table = [[0 for _ in range(capacity + 1)] for _ in range(len(denoms))]
        for index, denom in enumerate(denoms):
            for cap in range(capacity + 1):
                if cap == 0:
                    tracker_table[index][cap] = 1
                else:
                    if index > 0:
                        tracker_table[index][cap] = tracker_table[index - 1][cap]
                    if denom <= cap:
                        tracker_table[index][cap] += tracker_table[index][cap - denom]

        return tracker_table[len(denoms) - 1][capacity]


if __name__ == "__main__":
    x = CoinChange().dp_tabulation_soln([1, 2, 3], 5)
    print(x)
