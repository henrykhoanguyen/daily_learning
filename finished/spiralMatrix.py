from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rlen = len(matrix)
        clen = len(matrix[0])
        res = []
        k = 0
        l = 0

        while k < rlen and l < clen:

            # print from top row, left to right
            for i in range(l, clen):
                res.append(matrix[k][i])
            k += 1

            # print right bottom from top to bottom
            for i in range(k, rlen):
                res.append(matrix[i][clen-1])

            clen -= 1

            if k < rlen:
                # print bottom from left to right
                for i in range(clen-1, l-1, -1):
                    res.append(matrix[rlen-1][i])

                rlen -= 1

            if l < clen:
                # print left column from bottom to top
                for i in range(rlen - 1, k-1, -1):
                    res.append(matrix[i][l])
                l += 1

        print(res)
sol = Solution()
sol.spiralOrder(
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
)


sol.spiralOrder(
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
)