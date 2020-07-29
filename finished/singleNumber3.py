from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        nlen = len(nums)
        res = set()
        for i in range(nlen):
            if nums[i] not in res:
                res.add(nums[i])
            else:
                res.remove(nums[i])

        print(list(res))

sol = Solution()
sol.singleNumber([1,2,1,3,2,5])
sol.singleNumber([2,2,3,5,3,6,7,8,6,7])