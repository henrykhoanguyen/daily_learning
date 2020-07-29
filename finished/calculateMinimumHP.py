from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rlen = len(dungeon)
        clen = len(dungeon[0])

        hp = [[0] * clen for _ in range(rlen)]

        print(hp)

        for r in range(rlen-1, -1, -1):
            for c in range(clen-1, -1, -1):
                if r == rlen-1 and c == clen-1:
                    hp[r][c] = max(1, 1-dungeon[r][c])
                elif r == rlen - 1:
                    hp[r][c] = max(1, hp[r][c+1] - dungeon[r][c])
                elif c == clen - 1:
                    hp[r][c] = max(1, hp[r+1][c] - dungeon[r][c])
                else:
                    hp[r][c] = max(1, min(hp[r+1][c], hp[r][c+1]) - dungeon[r][c])

        print(hp[0][0])

sol = Solution()
sol.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
sol.calculateMinimumHP([[0,0]])