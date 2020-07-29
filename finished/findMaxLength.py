from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxLen, score = 0, 0
        tracker = {0:0}
        nlen = len(nums)

        for i in range(nlen):
            if nums[i] == 0:
                score -= 1
            elif nums[i] == 1:
                score += 1

            if score not in tracker:
                tracker[score] = i + 1
            else:
                maxLen = max(maxLen, i - tracker[score] + 1)

        print(maxLen)

sol = Solution()
sol.findMaxLength([0,1,0])
sol.findMaxLength([0,1])
sol.findMaxLength([0,0,0,0,1,1,1,0,0,1,1])