from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        res = -9999999999
        hlen = len(height)
        l = 0
        r = hlen - 1

        while l != r:
            tmp = min(height[r], height[l]) * (r - l)

            res = max(tmp, res)

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        print(res)

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])