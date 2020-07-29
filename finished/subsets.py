from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums

        res = [[]]
        for num in nums:
            res += [i + [num] for i in res]
        print(res)

sol = Solution()
sol.subsets([1,2,3])
sol.subsets([2,3])
