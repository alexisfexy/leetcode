from typing import List


class LongestPalSubSeqn(object):

    """
    Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
    In a palindromic subsequence, elements read the same backward and forward.

    A subsequence is a sequence that can be derived from another sequence
     by deleting some or no elements without changing the order of the remaining elements.

     Example:
        Input: "abdbca"
        Output: 5
        Explanation: LPS is "abdba".
    """

    def brute_force_soln(self, seq: List[str]) -> int:
        def _recursive_helper(check_front: int, check_back: int):
            if check_back >= len(seq) or check_front >= len(seq) or check_front > check_back:
                return 0
            front_val = seq[check_front]
            back_val = seq[check_back]
            if check_front == check_back:
                return 1
            elif front_val == back_val:
                return 2 + _recursive_helper(check_front+1, check_back-1)
            else:
                # Take front, move on back:
                front_sum = _recursive_helper(check_front, check_back-1)
                # Take back, move on front:
                back_sum = _recursive_helper(check_front+1, check_back)
                return max(front_sum, back_sum)
        return _recursive_helper(0, len(seq)-1)

    def dp_memo(self, seq: List[str]) -> int:
        cache = [[-1 for _ in range(len(seq))] for _ in range(len(seq))]

        def _recursive_helper(check_front: int, check_back: int):
            if check_back >= len(seq) or check_front >= len(seq) or check_front > check_back:
                return 0
            front_val = seq[check_front]
            back_val = seq[check_back]
            if check_front == check_back:
                return 1
            if cache[check_front][check_back] >= 0:
                return cache[check_front][check_back]
            if front_val == back_val:
                val = 2 + _recursive_helper(check_front+1, check_back-1)
            else:
                # Take front, move on back:
                front_sum = _recursive_helper(check_front, check_back-1)
                # Take back, move on front:
                back_sum = _recursive_helper(check_front+1, check_back)
                val = max(front_sum, back_sum)
            cache[check_front][check_back] = val
            return val
        return _recursive_helper(0, len(seq)-1)

if __name__ == "__main__":
    x = LongestPalSubSeqn().dp_memo("abdbca")
    print(x)
