
class FibNumbers(object):

    """
    Write a function to calculate the nth Fibonacci number.

    Fibonacci numbers are a series of numbers in which each number
    is the sum of the two preceding numbers.

    First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

    Mathematically we can define the Fibonacci numbers as:
    Fib(n) = Fib(n-1) + Fib(n-2), for n > 1
    Given that: Fib(0) = 0, and Fib(1) = 1
    """

    def brute_force_soln(self, n: int):
        def _recursive_helper(num: int):
            if num <= 1:
                return num
            return _recursive_helper(num-1) + _recursive_helper(num-2)
        return _recursive_helper(n)

    def dp_memoization_soln(self, n:  int):
        previously_calc = [-1 for _ in range(n+1)]

        def _recursive_helper(num: int):
            if previously_calc[num] >= 0:
                return previously_calc[num]
            val = num if num <= 1 else _recursive_helper(num-1) + _recursive_helper(num-2)
            previously_calc[num] = val
            return previously_calc[num]

        return _recursive_helper(n)

    def dp_tabulation_soln(self, n: int):
        tracker_table = [0 for _ in range(n+1)]
        for index, value in enumerate(tracker_table):
            if index < 2:
                tracker_table[index] = index
            else:
                tracker_table[index] = tracker_table[index-1] + tracker_table[index-2]
        return tracker_table[n]

    def optimized_soln(self, n: int):
        # We only care about the last two numbers
        if n < 2:
            return n
        num_1 = 0
        num_2 = 1
        sum_holder = None
        for _ in range(2, n+1):
            sum_holder = num_1 + num_2
            num_1 = num_2
            num_2 = sum_holder
        return num_2


if __name__ == "__main__":
    ans = FibNumbers().optimized_soln(6)
    print(ans)