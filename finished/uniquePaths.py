class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m+1) for _ in range(n+1)]

        # print(dp)
        for r in range(1,n+1):
            for c in range(1,m+1):
                if r == 1 and c == 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        print(dp[n][m])

sol = Solution()
sol.uniquePaths(3,2)
sol.uniquePaths(3,3)
sol.uniquePaths(7,3)
