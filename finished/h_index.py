'''
Problem: 272. H-index
Input: citations: List(int) -> a list of integer represents
        number of citations per paper
Output: int - a number of h-index
Explanation:
    First we sort the citations array in decrement order.
    Follow the math h-index = max(all min(f(i),i)) we will
    be able to find the h-index. This is a the first approach
    Run time for this is O(n) for n is the length of array.
    The second approach is sorting citations in incremental
    order, we then compare number of citation at each index
    with the difference of the length of citations and current
    index. If the citation is bigger than the difference,
    return the difference.
'''

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        clen = len(citations)

        res = []

        # Approach follow formula h-index = max( all min(f(i),i) )
        # citations = sorted(citations, reverse=True)
        # for index, num in enumerate(citations):
        #     res.append(min(index+1, num))
        #
        # print(res, max(res))
        # return max(res)

        citations.sort()

        for i in range(clen):
            if citations[i] >= clen - i:
                print(clen - i)
                return clen - i
        print(0)
        return 0
sol = Solution()
sol.hIndex([3,0,6,1,5])
sol.hIndex([10,8,5,4,3])
sol.hIndex([25,8,5,3,3])