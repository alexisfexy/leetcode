import math
from typing import List


class MaxRibbonCut(object):
    """
    We are given a ribbon of length ‘n’ and a set of possible ribbon lengths.
    We need to cut the ribbon into the maximum number of pieces that comply with
    the above-mentioned possible lengths.
    Write a method that will return the count of pieces.

    Example:
    n: 5
    Ribbon Lengths: {2,3,5}
    Output: 2
    Explanation: Ribbon pieces will be {2,3}.
    """
    def brute_force_soln(self, ribbon_lengths: List[int], goal_length: int) -> int:
        def _recursive_helper(remaining_len: int, current_index: int):
            if remaining_len == 0:
                return 0
            n_potential_lens = len(ribbon_lengths)
            if n_potential_lens == 0 or current_index >= n_potential_lens:
                return -math.inf
            else:
                curr_len = ribbon_lengths[current_index]
                _include_pieces = -math.inf
                if curr_len <= remaining_len:
                    _include_pieces = 1 + _recursive_helper(remaining_len-curr_len, current_index)
                _exclude_pieces = _recursive_helper(remaining_len, current_index+1)
                return max(_include_pieces, _exclude_pieces)
        return _recursive_helper(goal_length, 0)

    def dp_memoization(self, ribbon_lengths: List[int], goal_length: int) -> int:
        previously_calc = [[-1 for _ in range(goal_length+1)] for _ in range(len(ribbon_lengths))]
        def _recursive_helper(remaining_len: int, current_index: int):
            if remaining_len == 0:
                return 0
            n_potential_lens = len(ribbon_lengths)
            if n_potential_lens == 0 or current_index >= n_potential_lens:
                return -math.inf
            else:
                if previously_calc[current_index][remaining_len] != -1:
                    return previously_calc[current_index][remaining_len]
                curr_len = ribbon_lengths[current_index]
                _include_pieces = -math.inf
                if curr_len <= remaining_len:
                    _include_pieces = 1 + _recursive_helper(remaining_len - curr_len, current_index)
                _exclude_pieces = _recursive_helper(remaining_len, current_index + 1)
                previously_calc[current_index][remaining_len] = max(_include_pieces, _exclude_pieces)
                return previously_calc[current_index][remaining_len]
        return _recursive_helper(goal_length, 0)

    def dp_tabulation_soln(self, ribbon_lengths: List[int], goal_length: int) -> int:
        tracker_table = [[0 for _ in range(goal_length+1)] for _ in range(len(ribbon_lengths))]
        for index, curr_len in enumerate(ribbon_lengths):
            for goal_len in range(goal_length+1):
                if goal_len == 0:
                    tracker_table[index][goal_len] = 0
                else:
                    _include_sum, _exclude_sum = -math.inf, -math.inf
                    if curr_len <= goal_len:
                        _include_sum = 1 + tracker_table[index][goal_len-curr_len]
                    if index > 0:
                        _exclude_sum = tracker_table[index-1][goal_len]
                    tracker_table[index][goal_len] = max(_include_sum, _exclude_sum)
        return tracker_table[len(ribbon_lengths)-1][goal_length]


if __name__ == "__main__":
    ans = MaxRibbonCut().dp_tabulation_soln([3,5,7], 13)
    print(ans)