from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins:
            return 0
        if len(coins) == 1 and coins[0] < amount:
            return 0

        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        print(dp)
        return dp[amount]

sol = Solution()
sol.change(5, [1,2,5])