class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        def recurse(m, n):
            if m == 1 or n == 1:
                return 1
            if dp[m - 1][n - 1] != 0:
                return dp[m - 1][n - 1]
            else:
                dp[m - 1][n - 1] = recurse(m - 1, n) + recurse(m, n - 1)
                return dp[m - 1][n - 1]
        return recurse(m, n)