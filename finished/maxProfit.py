from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        plen = len(prices)

        for i in range(1, plen):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]
        print(total)

sol = Solution()
sol.maxProfit([7,6,4,3,1])
sol.maxProfit([1,2,3,4,5])
sol.maxProfit([7,1,5,3,6,4])