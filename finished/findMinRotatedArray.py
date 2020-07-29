from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        mini = 99999999
        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] < mini:
                mini = nums[mid]

            if nums[mid] >= nums[high]:
                low = mid+1
            else:
                high = mid
        print(mini)

sol = Solution()
sol.findMin([3,4,5,1,2])
sol.findMin([4,5,6,7,0,1,2])
sol.findMin([0,1,2,3,4,5,6])
sol.findMin([9,8,7,6,5,4,3,2])