from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rlen = len(grid)
        clen = len(grid[0])
        self.res = 0

        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] == 1:
                    self.res += 4

                    if r > 0 and grid[r - 1][c] == 1:
                        self.res -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        self.res -= 2

        print(self.res)
        ''' DFS/Flood Fill Approach '''
        # def dfs(grid, r, c):
        #     if r < 0 or r >= rlen or c < 0 or c >= clen or grid[r][c] == "#" or grid[r][c] == 0:
        #         return
        #
        #     if grid[r][c] == 1:
        #         self.res += 4
        #
        #     if r - 1 >= 0 and (grid[r-1][c] == 1 or grid[r-1][c] == "#"):
        #         self.res -= 1
        #     if r + 1 < rlen and (grid[r+1][c] == 1 or grid[r+1][c] == "#"):
        #         self.res -= 1
        #     if c - 1 >= 0 and (grid[r][c-1] == 1 or grid[r][c-1] == "#"):
        #         self.res -= 1
        #     if c + 1 < clen and (grid[r][c+1] == 1 or grid[r][c+1] == "#"):
        #         self.res -= 1
        #     grid[r][c] = "#"
        #     dfs(grid, r+1, c)
        #     dfs(grid, r-1, c)
        #     dfs(grid, r, c+1)
        #     dfs(grid, r, c-1)
        #
        # found = False
        # for r in range(rlen):
        #     for c in range(clen):
        #         if grid[r][c] == 1:
        #             dfs(grid, r, c)
        #             found = True
        #             break
        #     if found:
        #         break
        # print(self.res)

sol = Solution()
sol.islandPerimeter(
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
)