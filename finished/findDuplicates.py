'''
Problem: 442. Find All Duplicates in an Array
Input: an unsorted integer array list with
        1 <= a[i] <= n (n is size of array)
Output: an array list of duplicated integer
Explanation:
    Run time of this problem is O(n) for the
    most optimal solution. Since we know that
    1 <= a[i] <= n, we can visit other indexes
    within the array and "tag" it as visited.
    So, that when we visit a tagged index, we
    know that it is a duplicated. We then add
    that duplicate into our result array.
'''

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nlen = len(nums)
        res = []

        for num in nums:
            # if number is neg, then it
            # was visited before
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                # mark all visited number by
                # making it neg
                nums[abs(num) - 1] *= -1
                print(nums)
        print(res)

sol = Solution()
sol.findDuplicates([4,3,2,7,8,2,3,1])
sol.findDuplicates([3,2,7,4,8,6,5,2])
sol.findDuplicates([7,6,3,1,2,4,5])