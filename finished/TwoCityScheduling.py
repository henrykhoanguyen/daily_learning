from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        clen = len(costs)
        mid = clen // 2
        res = 0
        for i in range(clen):
            if i < mid:
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res

sol = Solution()
sol.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])