from typing import List


class LongestPalSubString(object):

    """
    Given a string, find the length of its Longest Palindromic Substring (LPS).
    In a palindromic string, elements read the same backward and forward.

     Example:
        Input: "abdbca"
        Output: 3
        Explanation: LPS is "bdb".

    Note: This problem follows the Longest Palindromic Subsequence pattern.
    The only difference is that in a palindromic subsequence characters can be non-adjacent,
    whereas in a substring all characters should form a palindrome. We will follow a similar approach though.
    """

    def brute_force_soln(self, letters: List[int]) -> int:
        def _recursive_helper(start_index: int, end_index: int):
            if start_index >= len(letters) or end_index >= len(letters) or end_index < start_index:
                return 0
            elif start_index == end_index:
                return 1
            else:
                start_val = letters[start_index]
                end_val = letters[end_index]
                if start_val == end_val:
                    # return 2 + _recursive_helper(start_index+1, end_index-1)  # If this was subsequence instead of substring!!
                    # If the values are the same, you have to check that the remaining substring is ALSO a palindrome
                    _remaining_pal = _recursive_helper(start_index + 1, end_index - 1)
                    _inbetween_letters = end_index-start_index-1
                    if _remaining_pal == _inbetween_letters:  # all remaining letters are a palindrome
                        return 2 + _remaining_pal
                _include_front = _recursive_helper(start_index, end_index-1)
                _include_back = _recursive_helper(start_index+1, end_index)
                return max(_include_back, _include_front)
        return _recursive_helper(0, len(letters)-1)


    def dp_memo_soln(self, letters: List[int]) -> int:
        n_letters = len(letters)
        cache = [[-1 for _ in range(n_letters)] for _ in range(n_letters)]
        def _recursive_helper(start_index: int, end_index: int):
            if start_index >= n_letters or end_index >= n_letters or end_index < start_index:
                return 0
            elif start_index == end_index:
                return 1
            else:
                if cache[start_index][end_index] >= 0:
                    return cache[start_index][end_index]
                start_val = letters[start_index]
                end_val = letters[end_index]
                if start_val == end_val:
                    # return 2 + _recursive_helper(start_index+1, end_index-1)  # If this was subsequence instead of substring!!
                    # If the values are the same, you have to check that the remaining substring is ALSO a palindrome
                    _remaining_pal = _recursive_helper(start_index + 1, end_index - 1)
                    _inbetween_letters = end_index-start_index-1
                    if _remaining_pal == _inbetween_letters:  # all remaining letters are a palindrome
                        cache[start_index][end_index] = 2 + _remaining_pal
                        return cache[start_index][end_index]
                _include_front = _recursive_helper(start_index, end_index-1)
                _include_back = _recursive_helper(start_index+1, end_index)
                cache[start_index][end_index] = max(_include_back, _include_front)
                return cache[start_index][end_index]
        return _recursive_helper(0, len(letters)-1)


if __name__ == "__main__":
    ans = LongestPalSubString().dp_memo_soln("abbdbca")
    print(ans)