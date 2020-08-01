'''
Problem: 309. Best Time to Buy and Sell Stock with Cooldown
Input: price: List[int]
Output: max profit - int
Explanation:
    Using state machine to understand and find the best time
    to buy and sell stock. StateOne is to buy, StateTwo is
    to hold and StateThree is to sell.
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        plen = len(prices)
        stateOne = [0] * plen
        stateTwo = [0] * plen
        stateThree = [0] * plen

        stateTwo[0] = -prices[0]
        stateThree[0] = -99999999

        for i in range(1, plen):
            stateOne[i] = max(stateThree[i - 1], stateOne[i - 1])
            stateTwo[i] = max(stateTwo[i - 1], stateOne[i - 1] - prices[i])
            stateThree[i] = stateTwo[i - 1] + prices[i]

        print( max(stateOne[plen - 1], stateThree[plen - 1]) )
        return max(stateOne[plen - 1], stateThree[plen - 1])

sol = Solution()
sol.maxProfit([1,2,3,0,2])