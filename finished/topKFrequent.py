from typing import List
from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        res = []
        dic = defaultdict()

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        sort = [[k,v] for k,v in sorted(dic.items(), key=lambda kv: kv[1], reverse=True)[:k]]
        print(sort)
        for i in sort:
            res.append(i[0])
        # print(dic)

        # Counter Approach
        # for i in Counter(nums).most_common(k):
        #     res.append(i[0])

        print(res)


sol = Solution()
sol.topKFrequent([1,1,1,1,2,2,3,3,3], 2)
sol.topKFrequent([1], 1)
sol.topKFrequent([-1,-1], 1)