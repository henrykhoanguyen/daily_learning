from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return

        nlen = len(nums)

        left, right = 0, nlen - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[left]:
                right = mid
                left += 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:       # nums[left] <= nums[mid] <= nums[high]
                right -= 1

        print(nums[left])

sol = Solution()
sol.findMin([1,3,5])
sol.findMin([2,2,2,3,0,1])
sol.findMin([7,8,1,4,4,5,6,7])
sol.findMin([2,3,4,5,6,7,1])
sol.findMin([7,8,9,9,1,2,2,2,2,3,4,6,7])
sol.findMin([3,3,3,3,3,1,1,3])
