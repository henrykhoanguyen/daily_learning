from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = curr = 0
        r = len(nums) - 1

        while curr <= r:
            if nums[curr] == 0:
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1
                curr += 1
            elif nums[curr] == 2:
                nums[r], nums[curr] = nums[curr], nums[r]
                r -= 1
            else:
                curr += 1
        print(nums)

sol = Solution()
sol.sortColors([2,0,2,1,1,0])
sol.sortColors([2,0,1,2,1,0,1,0])