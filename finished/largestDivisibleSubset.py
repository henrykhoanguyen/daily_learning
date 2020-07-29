from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        nlen = len(nums)
        dp = [1] * nlen
        maximum = 0

        if nlen == 0:
            return nums

        for i in range(1, nlen):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and 1+dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    if maximum < dp[i]:
                        maximum = dp[i]

        prev = -1
        for i in range(nlen-1, -1, -1):
            if dp[i] == maximum and (prev == -1 or prev % nums[i] == 0):
                res.append(nums[i])
                maximum -= 1
                prev = nums[i]
        print(res)

sol = Solution()
sol.largestDivisibleSubset([1,2,3])
sol.largestDivisibleSubset([1])
sol.largestDivisibleSubset([1,2,4,8])