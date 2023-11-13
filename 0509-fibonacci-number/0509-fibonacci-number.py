class Solution:
    def fib(self, n: int) -> int:
        if 0 <= n <= 1:
            return n

        fib_nums = [0] * (n+1)
        fib_nums[1] = 1

        for i in range(2, n + 1):
            fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]

        return fib_nums[n]