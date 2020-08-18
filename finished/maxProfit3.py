'''
Problem: 123. Best Time to Buy and Sell Stock III
Input:
    prices: List(int) -> the price of stock is selling on each day
Output:
    res: int -> result of max possible profit
Explanation:
    This is a dp problem. We traverse through prices array twice.
    Once from left to right to calculate the best possible 1 time
    transaction that yield highest profit. Second from right to
    left to calculate the best possible profit from 1 transaction.
    By doing this, we will be able to find different ways to make
    purchases that yield the best profit. Once we have find all
    possible ways to get best profit from 1 transaction, we store
    store each of the result in its respective array. Then, we
    traverse through both at the same and find the max sum profit
    from each day/cell. Return that max sum as final result profit.
    Run time for this is O(3n) or O(n). We have 3n because we
    have to traverse through same amount of days 3 times in 3
    separated loop.
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit1, profit2 = [0], [0]
        pMax1, pMax2 = prices[0], prices[-1]
        plen = len(prices)
        res = 0
        for i in range(1, plen):
            pMax1 = min(pMax1, prices[i])

            if prices[i] - pMax1 > profit1[-1]:
                profit1.append(prices[i] - pMax1)
            else:
                profit1.append(profit1[-1])

        for i in range(plen-2, -1, -1):
            pMax2 = max(pMax2, prices[i])

            if pMax2 - prices[i] > profit2[0]:
                profit2.insert(0, pMax2 - prices[i])
            else:
                profit2.insert(0, profit2[0])

        for i in range(plen):
            res = max(res, profit2[i] + profit1[i])
        print(res)


sol = Solution()
sol.maxProfit([3,3,5,0,0,3,1,4])
sol.maxProfit([1,2,3,4,5])
sol.maxProfit([7,6,4,3,1])
