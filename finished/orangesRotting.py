'''
Problem: 994. Rotting Oranges
Input: grid: List -> a grid of 0,1,2
        (0 - empty cell; 1 - good orange;
        2 - rotten orange)
Output: min - int -> time it take to turn all fresh to rotten orange
Explanation:
    We loop through whole grid to append any rotten oranges
    (cells with 2) into a queue and count number of fresh
    oranges (cells with 1). For base cases, if fresh count
    is 0, we return right the way, if fresh count is more
    than 1 but there are not any rotten oranges then we
    return -1 because it would be impossible to turn those
    fresh into rotten. If our queue is not empty, we start
    bfs on our first rotten orange and check all of its
    adjacent cells for fresh oranges. Once all possible
    fresh oranges are rotten, we increment minute count by
    1. The loop start all over again with the newest rotten
    oranges. Run time is O(n) for n is the number of oranges
    in grid. Space complexity is O(1) since we don't allocate
    any new memory.
'''

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rlen = len(grid)
        clen = len(grid[0])
        frontier = []
        fresh_count = 0

        for r in range(rlen):
            for c in range(clen):
                if grid[r][c] == 2:
                    frontier.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            print(0)
            return 0

        if fresh_count > 0 and not frontier:
            print(-1)
            return -1

        return self.bfs(grid,fresh_count, frontier)

    def bfs(self, grid, fresh_count, frontier):
        minutes = 0

        while frontier and fresh_count > 0:

            minutes += 1

            for _ in range(len(frontier)):
                row, col = frontier.pop(0)

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                    xx, yy = row + dx, col + dy

                    if xx < 0 or xx >= len(grid) or yy < 0 or yy >= len(grid[0]):
                        continue

                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    grid[xx][yy] = 2
                    fresh_count -= 1
                    frontier.append((xx, yy))

        print(minutes if fresh_count == 0 else -1)
        return minutes if fresh_count == 0 else -1

sol = Solution()
sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
sol.orangesRotting([[0,2]])
sol.orangesRotting([[2,2,2,2,1,1]])
sol.orangesRotting([[1]])