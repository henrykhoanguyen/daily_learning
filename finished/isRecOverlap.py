from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if not rec1 or not rec2:
            return False

        x, y = False, False

        if rec1[2] <= rec2[2]:
            x = self.helper([rec1[0], rec1[2]], [rec2[0], rec2[2]])
        else:
            x = self.helper([rec2[0], rec2[2]], [rec1[0], rec1[2]])

        if rec1[3] <= rec2[3]:
            y = self.helper([rec1[1], rec1[3]], [rec2[1], rec2[3]])
        else:
            y = self.helper([rec2[1], rec2[3]], [rec1[1], rec1[3]])

        print(x and y)
        return x and y

    def helper(self, rec1, rec2):
        if rec1[1] > rec2[0] and rec1[0] < rec2[1]:
            return True
        return False

sol = Solution()
sol.isRectangleOverlap([0,0,2,2], [1,1,3,3])
sol.isRectangleOverlap([0,0,1,1], [1,0,2,1])