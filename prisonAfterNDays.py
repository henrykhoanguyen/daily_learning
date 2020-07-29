from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells:
            return


sol = Solution()
sol.prisonAfterNDays([0,1,0,1,1,0,0,1], 7)
sol.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000)