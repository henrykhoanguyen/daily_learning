'''
Problem: 154. Find Minimum in Rotated Sorted Array 2
Input:  nums: List -> a sorted array list of integer
Output: int -> smallest number in sorted array
Explanation:
    Using Binary Search to quickly find the minimum
    in sorted array. There are 3 base cases in this
    problem. First case, if mid < right, then we know
    the smallest number is on the left side of the
    array. We move right = mid. Second case, if
    mid > right, then the smallest number is on the
    right side of the array, we move left = mid + 1.
    Third case, also the worst case possible, we
    find that mid == right. This would force us to
    compare mid and right linearly. aka one number
    as a time until we find the smallest number or
    traverse through the array if all numbers in
    the array are equal.
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nlen = len(nums)

        left, right = 0, nlen - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] == nums[right]:
                right -= 1

        print(nums[left])

sol = Solution()
sol.findMin([1,3,5])
sol.findMin([2,2,2,3,0,1])
sol.findMin([7,8,1,4,4,5,6,7])
sol.findMin([2,3,4,5,6,7,1])
sol.findMin([7,8,9,9,1,2,2,2,2,3,4,6,7])
sol.findMin([3,3,3,3,3,1,1,3])
