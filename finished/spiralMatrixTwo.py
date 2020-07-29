from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 1:
            return []
        if n == 1:
            return [[1]]
        res = [[0] * n for _ in range(n)]

        k,l = 0,0
        rlen = clen = n
        counter = 0
        while k < n and l < n:
            # top row from left to right
            for i in range(l, clen):
                counter += 1
                res[l][i] = counter
            k += 1

            # right most column from top to bottom
            for i in range(k, rlen):
                counter += 1
                res[i][clen-1] = counter

            clen -= 1

            # bottom row from right to left
            if k < rlen:
                for i in range(clen-1, l-1, -1):
                    counter += 1
                    res[rlen-1][i] = counter
                rlen -= 1

            # left most column from bottom to top
            if l < clen:
                for i in range(rlen-1, k-1, -1):
                    counter += 1
                    res[i][l] = counter
                l += 1

        print(res)

sol = Solution()
sol.generateMatrix(3)
sol.generateMatrix(4)
sol.generateMatrix(2)
