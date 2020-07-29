from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nlen = len(nums)

        low = 0
        high = nlen
        while low < high:
            mid = low + (high - low) // 2
            # print(mid, low, high)
            if nums[mid] == target:
                print(mid)
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1

        print(low)

sol = Solution()
sol.searchInsert([1,3,5,6], 5)
sol.searchInsert([1,3,5,6], 2)
sol.searchInsert([1,3,5,6], 7)
sol.searchInsert([1,3,5,6], 0)