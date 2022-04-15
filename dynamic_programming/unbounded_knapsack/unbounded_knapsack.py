from typing import List


class UnboundKnapsack(object):
    """
    Given the weights and profits of ‘N’ items:
        we are asked to put these items in a knapsack that has a capacity ‘C’.
        The goal is to get the maximum profit from the items in the knapsack.
        The only difference between the 0/1 Knapsack problem and
            this problem is that we are allowed to use an unlimited quantity of an item.

    Example:
        Items: { Apple, Orange, Melon }
        Weights: { 1, 2, 3 }
        Profits: { 15, 20, 50 }
        Knapsack capacity: 5

        Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5.

        5 Apples (total weight 5) => 75 profit
        1 Apple + 2 Oranges (total weight 5) => 55 profit
        2 Apples + 1 Melon (total weight 5) => 80 profit
        1 Orange + 1 Melon (total weight 5) => 70 profit

        This shows that 2 apples + 1 melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.
    """
    """
    The only difference between the 0/1 Knapsack problem and this one is:
     - after including the item, we recursively call to process all the items (including the current item). 
     In 0/1 Knapsack, however, we recursively call to process the remaining items.
    """

    def brute_force_soln(self, nums: List[int], weights: List[int], capacity: int):
        def _recursive_helper(nums: List[int], weights: List[int], capacity: int, current_index: int):
            if current_index >= len(nums) or capacity <= 0:
                return 0
            weight = weights[current_index]
            include_sum = 0
            if weight <= capacity:  # Include value, get max sum including this & including value itself
                include_sum = nums[current_index] + _recursive_helper(nums, weights, capacity - weight, current_index)
            exclude_sum = _recursive_helper(nums, weights, capacity,
                                            current_index + 1)  # Exclude sum. Advance index since we dont want this anymore
            return max(include_sum, exclude_sum)

        return _recursive_helper(nums, weights, capacity, 0)

    def dp_memoization_soln(self, nums: List[int], weights: List[int], capacity: int):
        previously_calc = [[-1 for _ in range(capacity + 1)] for _ in range(len(nums))]

        def _recursive_helper(nums: List[int], weights: List[int], capacity: int, current_index: int):
            if current_index >= len(nums) or capacity <= 0:
                return 0
            weight = weights[current_index]
            include_sum = 0
            if previously_calc[current_index][capacity] >= 0:
                return previously_calc[current_index][capacity]
            if weight <= capacity:  # Include value, get max sum including this & including value itself
                include_sum = nums[current_index] + _recursive_helper(nums, weights, capacity - weight, current_index)
            exclude_sum = _recursive_helper(nums, weights, capacity,
                                            current_index + 1)  # Exclude sum. Advance index since we dont want this anymore
            previously_calc[current_index][capacity] = max(include_sum, exclude_sum)
            return previously_calc[current_index][capacity]

        return _recursive_helper(nums, weights, capacity, 0)


if __name__ == "__main__":
    x = UnboundKnapsack().brute_force_soln([15, 20, 50], [1, 2, 3], 5)
    y = UnboundKnapsack().dp_memoization_soln([15, 20, 50], [1, 2, 3], 5)
    print(x)
    print(y)
