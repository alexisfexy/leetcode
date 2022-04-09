from typing import List


class Knapsack(object):
    """
    Given two integer arrays to represent weights and profits of ‘N’ items,
     we need to find a subset of these items which will give us maximum profit such that their cumulative weight
     is not more than a given number ‘C’. Write a function that returns the maximum profit.
     Each item can only be selected once, which means either we put an item in the knapsack or skip it.
    """

    def brute_force_solution(self, profits: List[int], weights: List[int], capacity: int) -> int:
        max_profits = set()
        for item_index, weight in enumerate(weights):
            profit = profits[item_index]
            running_profit: int = profit
            running_weight: int = weight
            for second_index in range(item_index, len(profits)):
                second_weight = weights[second_index]
                potential_weight = running_weight + second_weight
                if potential_weight <= capacity:
                    running_profit += profits[second_index]
                    running_weight = potential_weight
                elif second_weight + weight <= capacity and profits[second_index] + profit > running_profit:
                    running_profit = profit + profits[second_index]
                    running_weight = weight + second_weight
            max_profits.add(running_profit)
        return max(max_profits)

    def brute_force_recursive_soln(self, profits: List[int], weights: List[int], capacity: int) -> int:

        def _helper(profits: List[int], weights: List[int], capacity: int, current_index: int):
            if current_index >= len(weights) or capacity <= 0:
                return 0

            include_profit: int = 0
            weight: int = weights[current_index]
            if weight <= capacity:
                include_profit = profits[current_index] + _helper(profits, weights, capacity - weight,
                                                                  current_index + 1)

            exclude_profit = _helper(profits, weights, capacity, current_index + 1)
            return max(include_profit, exclude_profit)

        return _helper(profits, weights, capacity, 0)

    def dp_soln_memoization_recursive(self, profits: List[int], weights: List[int], capacity: int) -> int:
        # Remove all duplicate calculations
        # Store: [Capacity][Index]

        def _helper(previous_calcs: List[List[int]], profits: List[int], weights: List[int], capacity: int,
                    current_index: int):
            if current_index >= len(weights) or capacity <= 0:
                return 0

            # Seen this calc, return it:
            if previous_calcs[capacity][current_index] >= 0:
                return previous_calcs[capacity][current_index]

            include_profit: int = 0
            weight: int = weights[current_index]
            if weight <= capacity:
                include_profit = profits[current_index] + _helper(previous_calcs, profits, weights, capacity - weight,
                                                                  current_index + 1)

            exclude_profit = _helper(previous_calcs, profits, weights, capacity, current_index + 1)

            previous_calcs[capacity][current_index] = max(include_profit, exclude_profit)
            return max(include_profit, exclude_profit)

        previously_calculated = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]
        return _helper(previously_calculated, profits, weights, capacity, 0)

    def dp_soln_tabulation(self, profits: List[int], weights: List[int], capacity: int) -> int:
        tracker = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]
        for item_index in range(len(profits)):
            for cap in range(capacity + 1):
                if item_index == 0:  # First item only
                    tracker[item_index][cap] = profits[item_index] if weights[item_index] <= cap else 0
                # Weight of item is greater than capacity
                elif weights[item_index] > cap:
                    tracker[item_index][cap] = tracker[item_index - 1][cap]
                # Weight of item is equal or less than capacity:
                # Either: profit from item + max of remaining capacity
                # Or profit for capacity w/ one less item
                else:
                    remaining_cap = cap - weights[item_index]
                    include_profit = tracker[item_index][remaining_cap] + profits[item_index]
                    exclude_profit = tracker[item_index - 1][cap]
                    tracker[item_index][cap] = max(include_profit, exclude_profit)
        return tracker[len(profits) - 1][capacity]

    def dp_soln_tabulation_2d(self, profits: List[int], weights: List[int], capacity: int) -> int:
        pass



if __name__ == "__main__":
    max_profit = Knapsack().dp_solution_tabulation([1, 6, 10, 16], [1, 2, 3, 5], 7)
    print(max_profit)
