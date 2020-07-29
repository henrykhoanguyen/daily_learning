from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations) - 1

        while low <= high:
            mid = low + (high - low)//2

            if citations[mid] < (len(citations) - mid):
                low = mid + 1
            else:
                high = mid - 1

        print(len(citations) - low)

sol = Solution()
sol.hIndex([0,1,3,5,6])
sol.hIndex([10, 8, 5, 4, 3])
sol.hIndex([25, 8, 5, 3, 3])