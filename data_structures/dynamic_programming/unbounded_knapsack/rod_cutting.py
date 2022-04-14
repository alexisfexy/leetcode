from typing import List


class RodLength(object):
    """
    Given a rod of length ‘n’, we are asked to cut the rod
    and sell the pieces in a way that will maximize the profit.
    We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

    Lengths: [1, 2, 3, 4, 5]
    Prices: [2, 6, 7, 10, 13]
    Rod Length: 5

    Let’s try different combinations of cutting the rod:

    Five pieces of length 1 => 10 price
    Two pieces of length 2 and one piece of length 1 => 14 price
    One piece of length 3 and two pieces of length 1 => 11 price
    One piece of length 3 and one piece of length 2 => 13 price
    One piece of length 4 and one piece of length 1 => 12 price
    One piece of length 5 => 13 price

    This shows that we get the maximum price (14) by cutting the rod into two pieces of length ‘2’ and one piece of length ‘1’.
    """
    def brute_force_soln(self, lengths: List[int], prices: List[int], rod_length: int):

        def _recursive_helper(lengths: List[int], prices: List[int], remaining_length: int, current_index: int):
            if current_index >= len(lengths) or remaining_length <= 0:
                return 0
            current_len = lengths[current_index]
            current_price = prices[current_index]
            include_profit = 0
            if current_len <= remaining_length:
                include_profit = current_price + _recursive_helper(lengths, prices, remaining_length-current_len, current_index)
            exclude_profit = _recursive_helper(lengths, prices, remaining_length, current_index+1)
            return max(include_profit, exclude_profit)
        return _recursive_helper(lengths, prices, rod_length, 0)

    def dp_memoization_soln(self, lengths: List[int], prices: List[int], rod_length: int):
        previously_calc = [[-1 for _ in range(rod_length+1)] for _ in range(len(lengths))]

        def _recursive_helper(lengths: List[int], prices: List[int], remaining_length: int, current_index: int):
            if current_index >= len(lengths) or remaining_length <= 0:
                return 0
            if previously_calc[current_index][remaining_length] >= 0:
                return previously_calc[current_index][remaining_length]
            current_len = lengths[current_index]
            current_price = prices[current_index]
            include_profit = 0
            if current_len <= remaining_length:
                include_profit = current_price + _recursive_helper(lengths, prices, remaining_length - current_len,
                                                                   current_index)
            exclude_profit = _recursive_helper(lengths, prices, remaining_length, current_index + 1)
            previously_calc[current_index][remaining_length] = max(include_profit, exclude_profit)
            return previously_calc[current_index][remaining_length]

        return _recursive_helper(lengths, prices, rod_length, 0)

    def dp_tabulation_soln(self, lengths: List[int], prices: List[int], rod_length: int):
        tracker_table = [[0 for _ in range(rod_length + 1)] for _ in range(len(lengths))]

        for index, length in enumerate(lengths):
            price = prices[index]
            for rod_len in range(1, rod_length+1):
                include_profit, exclude_profit = 0, 0
                if length <= rod_len:
                    include_profit = price + tracker_table[index][rod_len-length]
                if index > 0:
                    exclude_profit = tracker_table[index-1][rod_len]
                tracker_table[index][rod_len] = max(include_profit, exclude_profit)
        return tracker_table[len(lengths)-1][rod_length]


if __name__ == "__main__":
    inputs = ([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5)
    x = RodLength().dp_memoization_soln(*inputs)
    y = RodLength().dp_tabulation_soln(*inputs)
    print(x)
    print(y)