from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        exist = {}
        nlen = len(nums)

        # Dictionary Approach
        # for i in range(nlen):
        #     if nums[i] not in dic:
        #         dic[nums[i]] = 1
        #         exist[nums[i]] = True
        #     else:
        #         dic[nums[i]] += 1
        #         if nums[i] in exist:
        #             del exist[nums[i]]
        # print([i for i in exist.keys()][0])

        nums.sort()

        if nums[0] != nums[1]:
            print(nums[0])
            return nums[0]
        if nums[-1] != nums[-2]:
            print(nums[-1])
            return nums[-1]

        for i in range(1, nlen, 3):
            if nums[i] != nums[i-1]:
                print(nums[i-1])
                return nums[i-1]

sol = Solution()
sol.singleNumber([2,2,3,2])
sol.singleNumber([0,1,0,1,0,1,99])
sol.singleNumber([99,0,1,0,1,0,1])
sol.singleNumber([2,4,2,4,3,2,4])
sol.singleNumber([2,3,2,3,3,2,4,5,6,5,6,5,6])
