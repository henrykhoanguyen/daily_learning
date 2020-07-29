from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rlen = len(obstacleGrid) - 1
        clen = len(obstacleGrid[0])
        visit = [[False] * rlen for _ in range(clen)]
        for r in range(rlen):
            for c in range(clen):
                if obstacleGrid[r][c] == 1:
                    visit[r][c] = True
        finished = 0


sol = Solution()
sol.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])

