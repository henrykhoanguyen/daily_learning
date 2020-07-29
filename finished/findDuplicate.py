from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nlen = len(nums)
        tor = hare = nums[0]

        # Find the loop/duplicate number in list
        while True:
            tor = nums[tor]
            hare = nums[nums[hare]]
            if tor == hare:
                break

        # Find the "entrance" of the duplicate
        tor = nums[0]
        while tor != hare:
            tor = nums[tor]
            hare = nums[hare]
        print(tor)
        return tor


sol = Solution()
sol.findDuplicate([1,3,4,2,2])
sol.findDuplicate([3,1,3,4,2])
sol.findDuplicate([3,1,2,4,3])
