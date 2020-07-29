from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nlen = len(numbers)
        # res = []
        # for i in range(nlen):
        #     if numbers[i] > target:
        #         break
        #     val = target - numbers[i]
        #     if val in numbers:
        #         res.append(i+1)
        # print(res)
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                print([dic[target-num]+1, i+1])
                return [dic[target-num]+1, i+1]
            dic[num] = i


sol = Solution()
sol.twoSum([2,7,11,15], 9)
sol.twoSum([2,3,4], 6)
sol.twoSum([2,7,11,15], 18)
sol.twoSum([2,7,11,15], 13)